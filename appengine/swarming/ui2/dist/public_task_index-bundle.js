!function(t){var e={};function n(s){if(e[s])return e[s].exports;var i=e[s]={i:s,l:!1,exports:{}};return t[s].call(i.exports,i,i.exports,n),i.l=!0,i.exports}n.m=t,n.c=e,n.d=function(t,e,s){n.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:s})},n.r=function(t){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},n.t=function(t,e){if(1&e&&(t=n(t)),8&e)return t;if(4&e&&"object"==typeof t&&t&&t.__esModule)return t;var s=Object.create(null);if(n.r(s),Object.defineProperty(s,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var i in t)n.d(s,i,function(e){return t[e]}.bind(null,i));return s},n.n=function(t){var e=t&&t.__esModule?function(){return t.default}:function(){return t};return n.d(e,"a",e),e},n.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},n.p="/newres/",n(n.s=16)}([function(t,e,n){"use strict";const s=new WeakMap,i=t=>(s.set(t,!0),t),r=t=>"function"==typeof t&&s.has(t),o=void 0!==window.customElements&&void 0!==window.customElements.polyfillWrapFlushCallback,a=(t,e,n=null,s=null)=>{let i=e;for(;i!==n;){const e=i.nextSibling;t.insertBefore(i,s),i=e}},l=(t,e,n=null)=>{let s=e;for(;s!==n;){const e=s.nextSibling;t.removeChild(s),s=e}},u={},c=`{{lit-${String(Math.random()).slice(2)}}}`,h=`\x3c!--${c}--\x3e`,d=new RegExp(`${c}|${h}`),m=(()=>{const t=document.createElement("div");return t.setAttribute("style","{{bad value}}"),"{{bad value}}"!==t.getAttribute("style")})();class p{constructor(t,e){this.parts=[],this.element=e;let n=-1,s=0;const i=[],r=e=>{const o=e.content,a=document.createTreeWalker(o,133,null,!1);let l,u;for(;a.nextNode();){n++,l=u;const e=u=a.currentNode;if(1===e.nodeType){if(e.hasAttributes()){const i=e.attributes;let r=0;for(let t=0;t<i.length;t++)i[t].value.indexOf(c)>=0&&r++;for(;r-- >0;){const i=t.strings[s],r=_.exec(i)[2],o=m&&"style"===r?"style$":/^[a-zA-Z-]*$/.test(r)?r:r.toLowerCase(),a=e.getAttribute(o).split(d);this.parts.push({type:"attribute",index:n,name:r,strings:a}),e.removeAttribute(o),s+=a.length-1}}"TEMPLATE"===e.tagName&&r(e)}else if(3===e.nodeType){const t=e.nodeValue;if(t.indexOf(c)<0)continue;const r=e.parentNode,o=t.split(d),a=o.length-1;s+=a;for(let t=0;t<a;t++)r.insertBefore(""===o[t]?g():document.createTextNode(o[t]),e),this.parts.push({type:"node",index:n++});r.insertBefore(""===o[a]?g():document.createTextNode(o[a]),e),i.push(e)}else if(8===e.nodeType)if(e.nodeValue===c){const t=e.parentNode,r=e.previousSibling;null===r||r!==l||r.nodeType!==Node.TEXT_NODE?t.insertBefore(g(),e):n--,this.parts.push({type:"node",index:n++}),i.push(e),null===e.nextSibling?t.insertBefore(g(),e):n--,u=l,s++}else{let t=-1;for(;-1!==(t=e.nodeValue.indexOf(c,t+1));)this.parts.push({type:"node",index:-1})}}};r(e);for(const t of i)t.parentNode.removeChild(t)}}const f=t=>-1!==t.index,g=()=>document.createComment(""),_=/([ \x09\x0a\x0c\x0d])([^\0-\x1F\x7F-\x9F \x09\x0a\x0c\x0d"'>=/]+)([ \x09\x0a\x0c\x0d]*=[ \x09\x0a\x0c\x0d]*(?:[^ \x09\x0a\x0c\x0d"'`<>=]*|"[^"]*|'[^']*))$/;class v{constructor(t,e,n){this._parts=[],this.template=t,this.processor=e,this.options=n}update(t){let e=0;for(const n of this._parts)void 0!==n&&n.setValue(t[e]),e++;for(const t of this._parts)void 0!==t&&t.commit()}_clone(){const t=o?this.template.element.content.cloneNode(!0):document.importNode(this.template.element.content,!0),e=this.template.parts;let n=0,s=0;const i=t=>{const r=document.createTreeWalker(t,133,null,!1);let o=r.nextNode();for(;n<e.length&&null!==o;){const t=e[n];if(f(t))if(s===t.index){if("node"===t.type){const t=this.processor.handleTextExpression(this.options);t.insertAfterNode(o),this._parts.push(t)}else this._parts.push(...this.processor.handleAttributeExpressions(o,t.name,t.strings,this.options));n++}else s++,"TEMPLATE"===o.nodeName&&i(o.content),o=r.nextNode();else this._parts.push(void 0),n++}};return i(t),o&&(document.adoptNode(t),customElements.upgrade(t)),t}}class b{constructor(t,e,n,s){this.strings=t,this.values=e,this.type=n,this.processor=s}getHTML(){const t=this.strings.length-1;let e="",n=!0;for(let s=0;s<t;s++){const t=this.strings[s];e+=t;const i=t.lastIndexOf(">");!(n=(i>-1||n)&&-1===t.indexOf("<",i+1))&&m&&(e=e.replace(_,(t,e,n,s)=>"style"===n?`${e}style$${s}`:t)),e+=n?h:c}return e+this.strings[t]}getTemplateElement(){const t=document.createElement("template");return t.innerHTML=this.getHTML(),t}}class y extends b{getHTML(){return`<svg>${super.getHTML()}</svg>`}getTemplateElement(){const t=super.getTemplateElement(),e=t.content,n=e.firstChild;return e.removeChild(n),a(e,n.firstChild),t}}const w=t=>null===t||!("object"==typeof t||"function"==typeof t);class x{constructor(t,e,n){this.dirty=!0,this.element=t,this.name=e,this.strings=n,this.parts=[];for(let t=0;t<n.length-1;t++)this.parts[t]=this._createPart()}_createPart(){return new E(this)}_getValue(){const t=this.strings,e=t.length-1;let n="";for(let s=0;s<e;s++){n+=t[s];const e=this.parts[s];if(void 0!==e){const t=e.value;if(null!=t&&(Array.isArray(t)||"string"!=typeof t&&t[Symbol.iterator]))for(const e of t)n+="string"==typeof e?e:String(e);else n+="string"==typeof t?t:String(t)}}return n+t[e]}commit(){this.dirty&&(this.dirty=!1,this.element.setAttribute(this.name,this._getValue()))}}class E{constructor(t){this.value=void 0,this.committer=t}setValue(t){t===u||w(t)&&t===this.value||(this.value=t,r(t)||(this.committer.dirty=!0))}commit(){for(;r(this.value);){const t=this.value;this.value=u,t(this)}this.value!==u&&this.committer.commit()}}class T{constructor(t){this.value=void 0,this._pendingValue=void 0,this.options=t}appendInto(t){this.startNode=t.appendChild(g()),this.endNode=t.appendChild(g())}insertAfterNode(t){this.startNode=t,this.endNode=t.nextSibling}appendIntoPart(t){t._insert(this.startNode=g()),t._insert(this.endNode=g())}insertAfterPart(t){t._insert(this.startNode=g()),this.endNode=t.endNode,t.endNode=this.startNode}setValue(t){this._pendingValue=t}commit(){for(;r(this._pendingValue);){const t=this._pendingValue;this._pendingValue=u,t(this)}const t=this._pendingValue;t!==u&&(w(t)?t!==this.value&&this._commitText(t):t instanceof b?this._commitTemplateResult(t):t instanceof Node?this._commitNode(t):Array.isArray(t)||t[Symbol.iterator]?this._commitIterable(t):void 0!==t.then?this._commitPromise(t):this._commitText(t))}_insert(t){this.endNode.parentNode.insertBefore(t,this.endNode)}_commitNode(t){this.value!==t&&(this.clear(),this._insert(t),this.value=t)}_commitText(t){const e=this.startNode.nextSibling;t=null==t?"":t,e===this.endNode.previousSibling&&e.nodeType===Node.TEXT_NODE?e.textContent=t:this._commitNode(document.createTextNode("string"==typeof t?t:String(t))),this.value=t}_commitTemplateResult(t){const e=this.options.templateFactory(t);if(this.value&&this.value.template===e)this.value.update(t.values);else{const n=new v(e,t.processor,this.options),s=n._clone();n.update(t.values),this._commitNode(s),this.value=n}}_commitIterable(t){Array.isArray(this.value)||(this.value=[],this.clear());const e=this.value;let n,s=0;for(const i of t)void 0===(n=e[s])&&(n=new T(this.options),e.push(n),0===s?n.appendIntoPart(this):n.insertAfterPart(e[s-1])),n.setValue(i),n.commit(),s++;s<e.length&&(e.length=s,this.clear(n&&n.endNode))}_commitPromise(t){this.value=t,t.then(e=>{this.value===t&&(this.setValue(e),this.commit())})}clear(t=this.startNode){l(this.startNode.parentNode,t.nextSibling,this.endNode)}}class k{constructor(t,e,n){if(this.value=void 0,this._pendingValue=void 0,2!==n.length||""!==n[0]||""!==n[1])throw new Error("Boolean attributes can only contain a single expression");this.element=t,this.name=e,this.strings=n}setValue(t){this._pendingValue=t}commit(){for(;r(this._pendingValue);){const t=this._pendingValue;this._pendingValue=u,t(this)}if(this._pendingValue===u)return;const t=!!this._pendingValue;this.value!==t&&(t?this.element.setAttribute(this.name,""):this.element.removeAttribute(this.name)),this.value=t,this._pendingValue=u}}class N extends x{constructor(t,e,n){super(t,e,n),this.single=2===n.length&&""===n[0]&&""===n[1]}_createPart(){return new C(this)}_getValue(){return this.single?this.parts[0].value:super._getValue()}commit(){this.dirty&&(this.dirty=!1,this.element[this.name]=this._getValue())}}class C extends E{}let A=!1;try{const t={get capture(){return A=!0,!1}};window.addEventListener("test",t,t),window.removeEventListener("test",t,t)}catch(t){}class L{constructor(t,e,n){this.value=void 0,this._pendingValue=void 0,this.element=t,this.eventName=e,this.eventContext=n}setValue(t){this._pendingValue=t}commit(){for(;r(this._pendingValue);){const t=this._pendingValue;this._pendingValue=u,t(this)}if(this._pendingValue===u)return;const t=this._pendingValue,e=this.value,n=null==t||null!=e&&(t.capture!==e.capture||t.once!==e.once||t.passive!==e.passive),s=null!=t&&(null==e||n);n&&this.element.removeEventListener(this.eventName,this,this._options),this._options=V(t),s&&this.element.addEventListener(this.eventName,this,this._options),this.value=t,this._pendingValue=u}handleEvent(t){("function"==typeof this.value?this.value:"function"==typeof this.value.handleEvent?this.value.handleEvent:()=>null).call(this.eventContext||this.element,t)}}const V=t=>t&&(A?{capture:t.capture,passive:t.passive,once:t.once}:t.capture);class M{handleAttributeExpressions(t,e,n,s){const i=e[0];return"."===i?new N(t,e.slice(1),n).parts:"@"===i?[new L(t,e.slice(1),s.eventContext)]:"?"===i?[new k(t,e.slice(1),n)]:new x(t,e,n).parts}handleTextExpression(t){return new T(t)}}const O=new M;function S(t){let e=H.get(t.type);void 0===e&&(e=new Map,H.set(t.type,e));let n=e.get(t.strings);return void 0===n&&(n=new p(t,t.getTemplateElement()),e.set(t.strings,n)),n}const H=new Map,$=new WeakMap,j=(t,e,n)=>{let s=$.get(e);void 0===s&&(l(e,e.firstChild),$.set(e,s=new T(Object.assign({templateFactory:S},n))),s.appendInto(e)),s.setValue(t),s.commit()};n.d(e,"c",function(){return P}),n.d(e,!1,function(){return b}),n.d(e,!1,function(){return y}),n.d(e,!1,function(){return c}),n.d(e,!1,function(){return h}),n.d(e,!1,function(){return d}),n.d(e,!1,function(){return m}),n.d(e,!1,function(){return p}),n.d(e,!1,function(){return f}),n.d(e,!1,function(){return g}),n.d(e,!1,function(){return _}),n.d(e,!1,function(){return M}),n.d(e,!1,function(){return O}),n.d(e,!1,function(){return v}),n.d(e,!1,function(){return u}),n.d(e,!1,function(){return w}),n.d(e,!1,function(){return x}),n.d(e,"a",function(){return E}),n.d(e,!1,function(){return T}),n.d(e,!1,function(){return k}),n.d(e,!1,function(){return N}),n.d(e,!1,function(){return C}),n.d(e,!1,function(){return L}),n.d(e,!1,function(){return o}),n.d(e,!1,function(){return a}),n.d(e,!1,function(){return l}),n.d(e,"b",function(){return i}),n.d(e,!1,function(){return r}),n.d(e,!1,function(){return $}),n.d(e,"d",function(){return j}),n.d(e,!1,function(){return S}),n.d(e,!1,function(){return H});const P=(t,...e)=>new b(t,e,"html",O)},function(t,e,n){"use strict";function s(t,e){if(t.hasOwnProperty(e)){let n=t[e];delete t[e],t[e]=n}}n.d(e,"a",function(){return s})},function(t,e,n){"use strict";function s(t,e=1e4){"object"==typeof t&&(t=t.message||JSON.stringify(t));var n={message:t,duration:e};document.dispatchEvent(new CustomEvent("error-sk",{detail:n,bubbles:!0}))}n.d(e,"a",function(){return s})},function(t,e,n){"use strict";function s(t){if(t.ok)return t.json();throw{message:`Bad network response: ${t.statusText}`,resp:t,status:t.status}}n.d(e,"a",function(){return s})},function(t,e,n){"use strict";n.d(e,"a",function(){return i});var s=n(0);const i=t=>Object(s.b)(e=>{if(void 0===t&&e instanceof s.a){if(t!==e.value){const t=e.committer.name;e.committer.element.removeAttribute(t)}}else e.setValue(t)})},,,,,function(t,e,n){"use strict";var s=n(2),i=n(0),r=n(4),o=n(3),a=n(1);window.customElements.define("toast-sk",class extends HTMLElement{constructor(){super(),this._timer=null}connectedCallback(){this.hasAttribute("duration")||(this.duration=5e3),Object(a.a)(this,"duration")}get duration(){return+this.getAttribute("duration")}set duration(t){this.setAttribute("duration",t)}show(){this.setAttribute("shown",""),this.duration>0&&!this._timer&&(this._timer=window.setTimeout(()=>{this._timer=null,this.hide()},this.duration))}hide(){this.removeAttribute("shown"),this._timer&&(window.clearTimeout(this._timer),this._timer=null)}});n(30);window.customElements.define("error-toast-sk",class extends HTMLElement{connectedCallback(){this.innerHTML="<toast-sk></toast-sk>",this._toast=this.firstElementChild,document.addEventListener("error-sk",this)}disconnectedCallback(){document.removeEventListener("error-sk",this)}handleEvent(t){t.detail.duration&&(this._toast.duration=t.detail.duration),this._toast.textContent=t.detail.message,this._toast.show()}});n(28);const l=document.createElement("template");l.innerHTML='<svg class="icon-sk-svg" xmlns="http://www.w3.org/2000/svg" width=24 height=24 viewBox="0 0 24 24"><path d="M20 8h-2.81c-.45-.78-1.07-1.45-1.82-1.96L17 4.41 15.59 3l-2.17 2.17C12.96 5.06 12.49 5 12 5c-.49 0-.96.06-1.41.17L8.41 3 7 4.41l1.62 1.63C7.88 6.55 7.26 7.22 6.81 8H4v2h2.09c-.05.33-.09.66-.09 1v1H4v2h2v1c0 .34.04.67.09 1H4v2h2.81c1.04 1.79 2.97 3 5.19 3s4.15-1.21 5.19-3H20v-2h-2.09c.05-.33.09-.66.09-1v-1h2v-2h-2v-1c0-.34-.04-.67-.09-1H20V8zm-6 8h-4v-2h4v2zm0-4h-4v-2h4v2z"/></svg>',window.customElements.define("bug-report-icon-sk",class extends HTMLElement{connectedCallback(){let t=l.content.cloneNode(!0);this.appendChild(t)}});const u=document.createElement("template");u.innerHTML='<svg class="icon-sk-svg" xmlns="http://www.w3.org/2000/svg" width=24 height=24 viewBox="0 0 24 24"><path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z"/></svg>',window.customElements.define("menu-icon-sk",class extends HTMLElement{connectedCallback(){let t=u.content.cloneNode(!0);this.appendChild(t)}}),window.customElements.define("spinner-sk",class extends HTMLElement{connectedCallback(){Object(a.a)(this,"active")}get active(){return this.hasAttribute("active")}set active(t){t?this.setAttribute("active",""):this.removeAttribute("active")}});n(27),n(26);window.customElements.define("oauth-login",class extends HTMLElement{connectedCallback(){Object(a.a)(this,"client_id"),Object(a.a)(this,"testing_offline"),this._auth_header="",this.testing_offline?this._profile={email:"missing@chromium.org",imageURL:"http://storage.googleapis.com/gd-wagtail-prod-assets/original_images/logo_google_fonts_color_2x_web_64dp.png"}:(this._profile=null,document.addEventListener("oauth-lib-loaded",()=>{gapi.auth2.init({client_id:this.client_id}).then(()=>{this._maybeFireLoginEvent(),this._render()},t=>{console.error(t),Object(s.a)(`Error initializing oauth: ${JSON.stringify(t)}`,1e4)})})),this._render()}static get observedAttributes(){return["client_id","testing_offline"]}get auth_header(){return this._auth_header}get client_id(){return this.getAttribute("client_id")}set client_id(t){return this.setAttribute("client_id",t)}get testing_offline(){return this.hasAttribute("testing_offline")}set testing_offline(t){t?this.setAttribute("testing_offline",!0):this.removeAttribute("testing_offline")}_maybeFireLoginEvent(){let t=gapi.auth2.getAuthInstance().currentUser.get();if(t.isSignedIn()){let e=t.getBasicProfile();this._profile={email:e.getEmail(),imageURL:e.getImageUrl()};let n=t.getAuthResponse(!0),s=`${n.token_type} ${n.access_token}`;return this.dispatchEvent(new CustomEvent("log-in",{detail:{auth_header:s},bubbles:!0})),this._auth_header=s,!0}return this._profile=null,this._auth_header="",!1}_logIn(){if(this.testing_offline)this._auth_header="Bearer 12345678910-boomshakalaka",this.dispatchEvent(new CustomEvent("log-in",{detail:{auth_header:this._auth_header},bubbles:!0})),this._render();else{let t=gapi.auth2.getAuthInstance();t&&t.signIn({scope:"email",prompt:"select_account"}).then(()=>{this._maybeFireLoginEvent()||console.warn("login was not successful; maybe user canceled"),this._render()})}}_logOut(){if(this.testing_offline)this._auth_header="",this._render(),window.location.reload();else{let t=gapi.auth2.getAuthInstance();t&&t.signOut().then(()=>{this._auth_header="",this._profile=null,window.location.reload()})}}_render(){Object(i.d)((t=>t.auth_header?i["c"]` <div> <img class=center id=avatar src="${t._profile.imageURL}" width=30 height=30> <span class=center>${t._profile.email}</span> <span class=center>|</span> <a class=center @click=${()=>t._logOut()} href="#">Sign out</a> </div>`:i["c"]` <div> <a @click=${()=>t._logIn()} href="#">Sign in</a> </div>`)(this),this)}attributeChangedCallback(t,e,n){this._render()}});const c=document.createElement("template");c.innerHTML="\n<button class=toggle-button>\n  <menu-icon-sk>\n  </menu-icon-sk>\n</button>\n";const h=document.createElement("template");h.innerHTML="\n<div class=spinner-spacer>\n  <spinner-sk></spinner-sk>\n</div>\n";const d=document.createElement("template");d.innerHTML='\n<a target=_blank rel=noopener\n   href="https://bugs.chromium.org/p/chromium/issues/entry?components=Infra%3EPlatform%3ESwarming%3EWebUI&owner=kjlubick@chromium.org&status=Assigned">\n  <bug-report-icon-sk class=fab></bug-report-icon-sk>\n</a>',window.customElements.define("swarming-app",class extends HTMLElement{constructor(){super(),this._busyTaskCount=0,this._spinner=null,this._dynamicEle=null,this._auth_header="",this._server_details={server_version:"You must log in to see more details",bot_version:""},this._permissions={}}connectedCallback(){Object(a.a)(this,"client_id"),Object(a.a)(this,"testing_offline"),this._addHTML(),this.addEventListener("log-in",t=>{this._auth_header=t.detail.auth_header,this._fetch()}),this._render()}static get observedAttributes(){return["client_id","testing_offline"]}get busy(){return!!this._busyTaskCount}get permissions(){return this._permissions}get server_details(){return this._server_details}get client_id(){return this.getAttribute("client_id")}set client_id(t){return this.setAttribute("client_id",t)}get testing_offline(){return this.hasAttribute("testing_offline")}set testing_offline(t){t?this.setAttribute("testing_offline",!0):this.removeAttribute("testing_offline")}addBusyTasks(t){this._busyTaskCount+=t,this._spinner&&this._busyTaskCount>0&&(this._spinner.active=!0)}finishedTask(){this._busyTaskCount--,this._busyTaskCount<=0&&(this._busyTaskCount=0,this._spinner&&(this._spinner.active=!1),this.dispatchEvent(new CustomEvent("busy-end",{bubbles:!0})))}_addHTML(){let t=this.querySelector("header"),e=t&&t.querySelector("aside"),n=this.querySelector("footer");if(!(t&&e&&e.classList.contains("hideable")))return;let s=c.content.cloneNode(!0);t.insertBefore(s,t.firstElementChild),(s=t.firstElementChild).addEventListener("click",t=>this._toggleMenu(t,e));let i=h.content.cloneNode(!0);t.insertBefore(i,e),this._spinner=t.querySelector("spinner-sk");let r=document.createElement("span");r.classList.add("grow"),t.appendChild(r),this._dynamicEle=document.createElement("div"),this._dynamicEle.classList.add("right"),t.appendChild(this._dynamicEle);let o=document.createElement("error-toast-sk");n.append(o);let a=d.content.cloneNode(!0);n.append(a)}_toggleMenu(t,e){e.classList.toggle("shown")}_fetch(){if(!this._auth_header)return;this._server_details={server_version:"<loading>",bot_version:"<loading>"};let t={headers:{authorization:this._auth_header}};this.addBusyTasks(2),fetch("/_ah/api/swarming/v1/server/details",t).then(o.a).then(t=>{this._server_details=t,this._render(),this.dispatchEvent(new CustomEvent("server-details-loaded",{bubbles:!0})),this.finishedTask()}).catch(t=>{403===t.status?(this._server_details={server_version:"User unauthorized - try logging in with a different account",bot_version:""},this._render()):(console.error(t),Object(s.a)(`Unexpected error loading details: ${t.message}`,5e3)),this.finishedTask()}),fetch("/_ah/api/swarming/v1/server/permissions",t).then(o.a).then(t=>{this._permissions=t,this._render(),this.dispatchEvent(new CustomEvent("permissions-loaded",{bubbles:!0})),this.finishedTask()}).catch(t=>{403!==t.status&&(console.error(t),Object(s.a)(`Unexpected error loading permissions: ${t.message}`,5e3)),this.finishedTask()})}_render(){this._dynamicEle&&Object(i.d)((t=>i["c"]` <div class=server-version> Server: <a href=${Object(r.a)(function(t){if(t&&t.server_version){var e=t.server_version.split("-");if(2===e.length)return`https://chromium.googlesource.com/infra/luci/luci-py/+/${e[1]}`}}(t._server_details))}> ${t._server_details.server_version} </a> </div> <oauth-login client_id=${t.client_id} ?testing_offline=${t.testing_offline}> </oauth-login>`)(this),this._dynamicEle)}attributeChangedCallback(t,e,n){this._render()}});n(25)},,,,,,,function(t,e,n){"use strict";n.r(e);n(9)},,,,,,,,,function(t,e){},function(t,e){},function(t,e){},function(t,e){},,function(t,e){}]);