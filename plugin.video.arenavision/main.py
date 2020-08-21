import sys
import xbmcgui
import xbmcplugin

addon_handle = int(sys.argv[1])



xbmcplugin.setContent(addon_handle, 'movies')
url = 'plugin://program.plexus/?mode=1&url=acestream://0e33a28fb9ea42e179c8a1d5a7d783567f3f666c&name=My+acestream+channel'
li = xbmcgui.ListItem('LaLigaTv', iconImage='DefaultVideo.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'plugin://program.plexus/?mode=1&url=acestream://66af8add3121a438f94051776ed28ed76b9d5c3e&name=My+acestream+channel'
li = xbmcgui.ListItem('Movistar LigadeCampeones', iconImage='DefaultVideo.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'plugin://program.plexus/?mode=1&url=acestream://2aabe1d62c475873d6644fc9ff0397e53aa4356b&name=My+acestream+channel'
li = xbmcgui.ListItem('Av5', iconImage='DefaultVideo.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'plugin://program.plexus/?mode=1&url=acestream://2aabe1d62c475873d6644fc9ff0397e53aa4356b&name=My+acestream+channel'
li = xbmcgui.ListItem('Av7', iconImage='DefaultVideo.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'plugin://program.plexus/?mode=1&url=acestream://349d10a91255b7ca495d595c31e7723006e5ebb1&name=My+acestream+channel'
li = xbmcgui.ListItem('Av9', iconImage='DefaultVideo.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'plugin://program.plexus/?mode=1&url=acestream://349d10a91255b7ca495d595c31e7723006e5ebb1&name=My+acestream+channel'
li = xbmcgui.ListItem('Movistar F1', iconImage='DefaultVideo.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'plugin://program.plexus/?mode=1&url=acestream://f98d848890d2d464b22c3f5d67c1b5603a5364f5&name=My+acestream+channel'
li = xbmcgui.ListItem('#Vamos', iconImage='DefaultVideo.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'plugin://program.plexus/?mode=1&url=acestream://34ca3cd827266e4a8de786a453ff6a177fdf2a6b&name=My+acestream+channel'
li = xbmcgui.ListItem('Movistar Deportes', iconImage='DefaultVideo.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://127.0.0.1:6878/ace/manifest.m3u8?url=https://xxx.dailysportlist.xyz/1/1.m3u8'
li = xbmcgui.ListItem('Daily CH1', iconImage='DefaultVideo.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://127.0.0.1:6878/ace/manifest.m3u8?url=https://xxx.dailysportlist.xyz/4/4.m3u8'
li = xbmcgui.ListItem('Daily CH3', iconImage='DefaultVideo.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)


xbmcplugin.endOfDirectory(addon_handle)