const electron = require('electron')
const app = electron.app
const BrowserWindow = electron.BrowserWindow


function createWindow() {
  window = new BrowserWindow({
      width: 550,
      height: 350,
      frame: false,
      transparent: true,
      resizable: false,
      alwaysOnTop: true,
      webPreferences: {
          nodeIntegration: true,
          contextIsolation: false,
          enableRemoteModule: true
      }
  })
  window.loadFile('pages/menu/menu.html')

  // window.webContents.openDevTools()

  window.on('closed', () => {
      window = null
  })
}

app.on('ready', createWindow)

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
      app.quit()
  }
})

app.on('activated', () => {
  if (window === null) {
      createWindow()
  }
})
