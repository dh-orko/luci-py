// Copyright 2018 The LUCI Authors. All rights reserved.
// Use of this source code is governed under the Apache License, Version 2.0
// that can be found in the LICENSE file.

/** @module swarming-ui/SwarmingAppBoilerplate */

import { errorMessage } from "elements-sk/errorMessage";
import { render } from "lit-html";
import { upgradeProperty } from "elements-sk/upgradeProperty";
import { TasksService } from "./services/tasks";
import { BotsService } from "./services/bots";

/** @classdesc
 * The SwarmingAppBoilerplate class deduplicates much of the boilerplate
 * that all top-level Swarming apps (e.g. bot-list, task-page) have.
 *
 * To use, extend SwarmingAppBoilerplate, call <code>super(template)</code> in
 * the constructor with the main template that should be rendered, and call
 * <code>super.connectedCallback()</code> in the
 * <code>connectedCallback()</code> function to get access to the attributes.
 *
 * @example
 * const template = (ele) => html`<h1>Hello ${ele.foo}</h1>`
 *
 * window.customElements.define('my-page', class extends SwarmingAppBoilerplate {
 *
 *  constructor() {
 *    super(template);
 *    this.foo = 'World';
 *  }
 *
 *  connectedCallback() {
 *   super.connectedCallback();
 *  }
 *}
 *
 * @attr testing_offline - If true, the real login flow won't be used.
 *    Instead, dummy data will be used. Ideal for local testing.
 *
 */
export default class SwarmingAppBoilerplate extends HTMLElement {
  constructor(template) {
    super();
    this._template = template;
    this._app = null;
    this._auth_header = "";
    this._profile = null;
    // False until we see a 403 and get a call to setUserNotAuthorized();
    this._notAuthorized = false;
  }

  connectedCallback() {
    upgradeProperty(this, "testing_offline");

    this._authHeaderEvent = (e) => {
      this._auth_header = e.detail.authHeader;
    };
    this.addEventListener("log-in", this._authHeaderEvent);
  }

  disconnectedCallback() {
    this.removeEventListener("log-in", this._authHeaderEvent);
  }

  static get observedAttributes() {
    return ["testing_offline"];
  }

  /** @prop {HTMLElement} app - A reference to the embedded &lt;swarming-app&gt
                        which is available after the first render() call.
                        Read only.*/
  get app() {
    return this._app;
  }

  /** @prop {string} authHeader - reflects the authHeader passed up from the
                        &lt;oauth-login&gt;.
                        Read only.*/
  get authHeader() {
    return this._auth_header;
  }

  /** @prop {boolean} loggedIn Indicates if a user is logged in and authorized
                        to see this page.
   *                    Read-only. */
  get loggedInAndAuthorized() {
    return !!this._auth_header && !this._notAuthorized;
  }

  /** @prop {Object} permissions - reflects the permissions from the
                        included &lt;swarming-app&gt;
                        Read only.*/
  get permissions() {
    return (this._app && this._app.permissions) || {};
  }

  /** @prop {Object} profile An object with keys email and imageURL of the
                             logged in user. Read Only. */
  get profile() {
    return (this._app && this._app.profile) || {};
  }

  /** @prop {Object} server_details - reflects the server_details from the
                        included &lt;swarming-app&gt;
                        Read only.*/
  get serverDetails() {
    return (this._app && this._app.serverDetails) || {};
  }

  /** @prop {bool} testing_offline Mirrors the attribute 'testing_offline'. */
  // eslint-disable-next-line camelcase
  get testing_offline() {
    return this.hasAttribute("testing_offline");
  }
  // eslint-disable-next-line camelcase
  set testing_offline(val) {
    if (val) {
      this.setAttribute("testing_offline", true);
    } else {
      this.removeAttribute("testing_offline");
    }
  }

  /** Handles handles an error from prpc client, possibly signaling the user
   * isn't authorized to see this page.
      @param {Object} e - The error given prpc client.
      @param {String} loadingWhat - A short string to describe what failed.
                      (e.g. bots/list if the bots/list endpoint was queried)
      @param {boolean} ignoreAuthError - A flag to ignore 403 error.
   */
  prpcError(e, loadingWhat, ignoreAuthError) {
    if (e.codeName === "PERMISSION_DENIED") {
      this._message =
        "User unauthorized - try logging in " + "with a different account";
      this._notAuthorized = true;
      this.render();
      this._app.finishedTask();
    } else {
      this.fetchError(e, loadingWhat, ignoreAuthError);
    }
  }

  /** Handles a fetch error, possibly signaling the user isn't authorized to
      see this page.
      @param {Object} e - The error given by fetch.
      @param {String} loadingWhat - A short string to describe what failed.
                      (e.g. bots/list if the bots/list endpoint was queried)
      @param {boolean} ignoreAuthError - A flag to ignore 403 error.
   */
  fetchError(e, loadingWhat, ignoreAuthError) {
    if (e.status === 403 && !ignoreAuthError) {
      this._message =
        "User unauthorized - try logging in " + "with a different account";
      this._notAuthorized = true;
      this.render();
    } else if (e.name !== "AbortError") {
      // We can ignore AbortError since they fire anytime a filter is added
      // or removed (even for fetch promises that have already been resolved).
      // Chrome and Firefox report a DOMException in this case:
      // https://developer.mozilla.org/en-US/docs/Web/API/DOMException
      console.error(e);
      errorMessage(
        `Unexpected error loading ${loadingWhat}: ${e.message}`,
        5000
      );
    }
    this._app.finishedTask();
  }

  /** Re-renders the app, starting with the top level template. */
  render() {
    render(this._template(this), this, { eventContext: this });
    if (!this._app) {
      this._app = this.firstElementChild;
      // render again in case anything was using attributes on this._app.
      render(this._template(this), this, { eventContext: this });
    }
  }

  attributeChangedCallback(attrName, oldVal, newVal) {
    this.render();
  }

  _createTasksService() {
    return new TasksService(this.authHeader, this._fetchController.signal);
  }

  _createBotService() {
    return new BotsService(this.authHeader, this._fetchController.signal);
  }
}
