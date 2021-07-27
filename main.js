const electron = require('electron')
const app = electron.app
const BrowserWindow = electron.BrowserWindow


function createWindow() {
  window = new BrowserWindow({
      width: 350,
      height: 700,
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
  window.loadFile('index.html')

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
