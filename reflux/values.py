import pkg_resources

js_path = pkg_resources.resource_filename(__name__, "templates/reflux.js")
css_path = pkg_resources.resource_filename(__name__, "templates/reflux.css")

JS = """javascript:(function() {let p1 = document.getElementById("reflux-theme");let p2 = document.getElementById("reflux-display");if (p1 && p2) {var go = confirm("There is a Reflux theme already running. Would you like to stop it?");if (go) {p1.remove();p2.remove();alert("This theme has been stopped.");} else {alert("This theme will continue running.");}} else {var go = confirm("Run this Reflux Theme?\n\nName: !name!\nAuthor: !author!\nDescription: !description!");if (go) {var style = document.createElement("style");var head = document.getElementsByTagName("head")[0];var target = document.getElementsByClassName("jsx-3593981321")[0];style.setAttribute("id", "reflux-theme");style.appendChild(document.createTextNode(`!css!`));
target.insertAdjacentHTML("afterend", `<a id="reflux-display" class="jsx-3593981321" target="_blank" href="//reflux.repl.co/"><span class="jsx-3593981321 sidebar-layout-nav-item-icon"><svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="24" height="24" viewBox="0 0 172 172" style="fill:#000000;"><g fill="none" fill-rule="nonzero" stroke="none" stroke-width="1" stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="10" stroke-dasharray="" stroke-dashoffset="0" font-family="none" font-weight="none" font-size="none" text-anchor="none" style="mix-blend-mode: normal"><path d="M0,172v-172h172v172z" fill="none"></path><g fill="#00d1b2"><path d="M35.83333,21.5c-7.91917,0 -14.33333,6.41417 -14.33333,14.33333v100.33333c0,7.90483 6.4285,14.33333 14.33333,14.33333h100.33333c7.90483,0 14.33333,-6.4285 14.33333,-14.33333v-100.33333c0,-7.91917 -6.41417,-14.33333 -14.33333,-14.33333zM35.83333,35.83333h100.33333v14.33333h-100.33333zM35.83333,64.5h100.33333v71.66667h-100.33333zM71.66667,77.34961l-22.98372,22.98372l22.98372,22.98372l7.16667,-7.16667l-15.81706,-15.81706l15.81706,-15.81706zM100.33333,77.34961l-7.16667,7.16667l15.81706,15.81706l-15.81706,15.81706l7.16667,7.16667l22.98372,-22.98372z"></path></g></g></svg></span><div class="jsx-3593981321">Reflux</div><div class="jsx-3593981321 beta-label"><div style="background-color: #6262ff;" class="jsx-4210545632 beta-tag">ON</div></div></a>`);head.appendChild(style);alert("Reflux is now running!");} else {alert("Reflux operation cancelled.");}}})();"""
CSS = """.replit-ui-theme-root.dark{!css!}.replit-ui-theme-root.light{!css!}"""
BASE_TOKENS = [f"span.mtk{n}" for n in range(8)]

TOKENS = [
    "keyword",
    "string",
    "comment",
    "variable",
    "punctuation",
    "constant.other",
    "constant.language",
    "constant.numeric",
    "parameter.variable",
    "function.support",
    "storage.type",
    "paren.rparen",
    "lparen.paren"
]

DEFAULT = {
    "name": None,
    "author": None,
    "description": None,
    "default": "light"
}

COLORS = {
    "dark": {
        "background-1": "#1d2333",
        "background-2": "#171d2d",
        "background-3": "#0e1525",
        "control-1": "#313646",
        "control-2": "#2b3140",
        "control-3": "#262b3b",
        "border": "#313646",
        "foreground-1": "#e1e2e4",
        "foreground-2": "#90939c",
        "foreground-3": "#696d78",
        "foreground-4": "#4e525f",
        "foreground-transparent-1": "rgba(14, 21, 37, 0.48)",
        "foreground-transparent-2": "rgba(14, 21, 37, 0.24)",
        "foreground-transparent-3": "rgba(14, 21, 37, 0.12)",
        "primary-1": "#3485e4",
        "primary-2": "#337bd2",
        "primary-3": "#3273c4",
        "primary-4": "#316cb8",
        "primary-transparent-1": "rgba(52, 133, 228, 0.48)",
        "primary-transparent-2": "rgba(52, 133, 228, 0.24)",
        "primary-transparent-3": "rgba(52, 133, 228, 0.12)",
        "negative-1": "#ff491c",
        "negative-2": "#eb451b",
        "negative-3": "#db411b",
        "negative-4": "#cd3e1a",
        "negative-transparent-1": "rgba(255, 73, 28, 0.48)",
        "negative-transparent-2": "rgba(255, 73, 28, 0.24)",
        "negative-transparent-3": "rgba(255, 73, 28, 0.12)",
        "warning-1": "#f26702",
        "warning-2": "#de5f07",
        "warning-3": "#ce590a",
        "warning-4": "#c0540c",
        "warning-transparent-1": "rgba(242, 103, 2, 0.48)",
        "warning-transparent-2": "rgba(242, 103, 2, 0.24)",
        "warning-transparent-3": "rgba(242, 103, 2, 0.12)",
        "positive-1": "#20ab46",
        "positive-2": "#219d41",
        "positive-3": "#22923d",
        "positive-4": "#22883a",
        "positive-transparent-1": "rgba(24, 204, 81, 0.48)",
        "positive-transparent-2": "rgba(24, 204, 81, 0.24)",
        "positive-transparent-3": "rgba(24, 204, 81, 0.12)"
    },
    "light": {
        "background-1": "#ffffff",
        "background-2": "#f6f6f6",
        "background-3": "#eeeeee",
        "control-1": "#e0e0e0",
        "control-2": "#e9e9e9",
        "control-3": "#f3f3f3",
        "border": "#e0e0e0",
        "foreground-1": "#363636",
        "foreground-2": "#6f6f6f",
        "foreground-3": "#949494",
        "foreground-4": "#b7b7b7",
        "foreground-transparent-1": "rgba(255, 255, 255, 0.48)",
        "foreground-transparent-2": "rgba(255, 255, 255, 0.24)",
        "foreground-transparent-3": "rgba(255, 255, 255, 0.12)",
        "primary-1": "#3485e4",
        "primary-2": "#337ad1",
        "primary-3": "#3272c2",
        "primary-4": "#316ab4",
        "primary-transparent-1": "rgba(52, 133, 228, 0.48)",
        "primary-transparent-2": "rgba(52, 133, 228, 0.24)",
        "primary-transparent-3": "rgba(52, 133, 228, 0.12)",
        "negative-1": "#ff491c",
        "negative-2": "#e9441b",
        "negative-3": "#d8411b",
        "negative-4": "#c93d1a",
        "negative-transparent-1": "rgba(255, 73, 28, 0.48)",
        "negative-transparent-2": "rgba(255, 73, 28, 0.24)",
        "negative-transparent-3": "rgba(255, 73, 28, 0.12)",
        "warning-1": "#eb6404",
        "warning-2": "#d65c08",
        "warning-3": "#c7560b",
        "warning-4": "#b8510d",
        "warning-transparent-1": "rgba(242, 103, 2, 0.48)",
        "warning-transparent-2": "rgba(242, 103, 2, 0.24)",
        "warning-transparent-3": "rgba(242, 103, 2, 0.12)",
        "positive-1": "#21a243",
        "positive-2": "#21953e",
        "positive-3": "#228a3a",
        "positive-4": "#228037",
        "positive-transparent-1": "rgba(24, 204, 81, 0.48)",
        "positive-transparent-2": "rgba(24, 204, 81, 0.24)",
        "positive-transparent-3": "rgba(24, 204, 81, 0.12)"
    }
}
