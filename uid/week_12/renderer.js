const nodeVersion = document.getElementById("node-version");
const chromeVersion = document.getElementById("chrome-version");
const electronVersion = document.getElementById("electron-version");

nodeVersion.textContent = window.versions.node();
chromeVersion.textContent = window.versions.chrome();
electronVersion.textContent = window.versions.electron();
