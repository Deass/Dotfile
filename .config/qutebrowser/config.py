import subprocess
config.load_autoconfig()

# variables
black    = "#000000"
darkgrey = "#030303"
magenta  = "#ff009e"
midgrey  = "#544d4d"
pink     = "#ff00f3"
red      = "#ff0000"
white    = "#ffffff"
yellow   = "#ffdb00"
blue     = "#005577"

#Bindingsinginnit.
config.bind('xc', 'config-cycle tabs.show always never')
config.bind('xx', 'set tabs.show always;; later 5000 set tabs.show switching')
#config.bind('xb', 'set statusbar.show always;; later 5000 set statusbar.show never')
config.bind('<Tab>', 'set tabs.show always;; later 9000 set tabs.show switching')
config.bind('xg', 'tab-give')
config.bind('zd', 'download-open')
config.bind('B', 'set-cmd-text -s :bookmark-load')
config.bind('xs', 'config-source')
config.bind('<Alt+Up>', 'tab-prev')
config.bind('<Alt+Down>', 'tab-next')
config.bind('<Alt+Right>', 'tab-give')
config.bind('<Ctrl-h>', 'set-cmd-text :help :')
config.bind('e', 'set-cmd-text -s :tab-select')
config.bind('<Alt-f>', 'hint inputs')
config.bind('<Ctrl-e>', 'open-editor')
config.bind('<z><l>', 'spawn --userscript qute-pass')
config.bind('<z><u><l>', 'spawn --userscript qute-pass --username-only')
config.bind('<z><p><l>', 'spawn --userscript qute-pass --password-only')
config.bind('<z><o><l>', 'spawn --userscript qute-pass --otp-only')

#Downloading keys
c.downloads.location.directory = '~/Downloads'
c.downloads.location.prompt = True
config.bind(',d', 'set downloads.location.directory ~/Downloads/;; hint links download')
config.bind(',i', 'set downloads.location.directory ~/Pictures/;; hint images download')
config.bind(',o', 'set downloads.location.directory ~/mnt/rust/obs/;; hint links download')
config.bind('<Ctrl-o>', 'prompt-open-download', mode='prompt')

# Ctrl shortcuts run scripts / applications
config.bind('<Ctrl-m>', 'spawn mpv --volume=100 --ytdl-format=bestvideo[height<=?480]+bestaudio/best {url}')
config.bind('<Ctrl-Shift-p>', 'spawn --userscript password_fill')
config.bind('<Alt-p>','spawn --userscript password_fill')
config.bind('<Ctrl-r>', 'spawn --userscript readability')
config.bind('<Ctrl-y>', 'hint links spawn mpv --volume=50 {hint-url}')

# This one is a special one that opens all my pinned tabs
config.bind('xo','open https://www.youtube.com/dashboard;;tab-pin;;open -t https://hexdsl.co.uk;;tab-pin;;open -t http://localhost:8081/home/;;tab-pin;;open -t http://localhost:9091/transmission/web/#confirm;;tab-pin')

# Unbind shite default
config.unbind('<Ctrl-w>')
config.unbind('q')
config.unbind('v')
config.unbind('V')
#config.unbind('z')
config.unbind('<Ctrl-v>')

c.scrolling.bar = 'never'
c.statusbar.show = 'always'
c.content.autoplay = False
c.tabs.background = True
c.auto_save.session = True
c.colors.webpage.preferred_color_scheme = 'dark'
c.content.blocking.adblock.lists = ['https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2020.txt', 'https://easylist.to/easylist/easylist.txt', 'https://easylist.to/easylist/easyprivacy.txt','/home/hexdsl/.config/qutebrowser/lol.txt']
c.content.blocking.method = 'both'
c.content.notifications.enabled = False
c.content.cookies.accept = 'all'
c.content.tls.certificate_errors = 'load-insecurely'
c.content.fullscreen.window = True
c.content.geolocation = 'ask'
#c.content.user_stylesheets = '~/.config/qutebrowser/lol.css'
c.completion.open_categories = ['quickmarks', 'searchengines', 'history']
c.content.webgl = True
c.downloads.remove_finished = 5000
c.editor.command = ["alacritty", "-e", "nvim", "{}"]
c.messages.timeout = 5000
c.content.fullscreen.overlay_timeout = 0
c.scrolling.smooth = True
c.spellcheck.languages = ['en-GB']
c.tabs.favicons.scale = 1
c.tabs.indicator.padding = {"top": 0, "right": 0, "bottom": 0, "left": 0}
c.tabs.indicator.width = 0
c.tabs.padding = {"top": 2, "right": 2, "bottom": 2, "left": 2}
c.tabs.position = "top"
c.tabs.show = "switching"
#c.tabs.title.format = '{index:>02}'
#c.tabs.title.format_pinned = '{index:>02}'
c.tabs.width = 54
c.url.open_base_url = True
c.zoom.default = '100%'
c.completion.shrink = True

# search engine shortneners
c.url.searchengines = {
"DEFAULT":"https://duckduckgo.com/?q={}",
"goog": "https://www.google.co.uk/search?&q={}",
"googi": "https://www.google.co.uk/search?q={}&tbm=isch",
"wiki": "https://en.wikipedia.org/w/index.php?search={}",
"wiby": "https://wiby.me/?q={}",
"steam": "http://store.steampowered.com/search/?term={}",
"ddg": "https://duckduckgo.com/?q={}",
"imdb": "http://www.imdb.com/find?ref_=nv_sr_fn&s=all&q={}",
"dic": "http://www.dictionary.com/browse/{}",
"ety": "http://www.etymonline.com/index.php?allowed_in_frame=0&search={}",
"urban": "http://www.urbandictionary.com/define.php?term={}",
"ddgi": "https://duckduckgo.com/?q={}&iar=images",
"lutris": "https://lutris.net/games/?q={}",
"deal": "https://isthereanydeal.com/search/?q={}",
"gog": "https://www.gog.com/games?sort=popularity&search={}&page=1",
"proton": "https://www.protondb.com/search?q={}",
"qwant": "https://www.qwant.com/?q={}",
"sp": "https://www.startpage.com/do/dsearch?query={}",
"humble": "https://www.humblebundle.com/store/search?sort=bestselling&search={}",
"tor": "https://www.magnetdl.com/search/?m=1&q={}",
"torrent": "https://www.magnetdl.com/search/?m=1&q={}",
"tom": "https://www.rottentomatoes.com/search?search={}",
"itch": "https://itch.io/search?q={}"}

#colours
c.fonts.contextmenu = 'JetBrainsMono Nerd Font'
c.fonts.default_family = 'JetBrainsMono Nerd Font'
c.fonts.default_size = "10pt"
c.completion.scrollbar.width = 0
c.colors.completion.category.bg = black
c.colors.completion.category.bg = darkgrey
c.colors.completion.category.border.bottom = blue
c.colors.completion.category.border.top = darkgrey
c.colors.completion.category.border.top = darkgrey
c.colors.completion.category.fg = white
c.colors.completion.category.fg = white
c.colors.completion.even.bg = midgrey
c.colors.completion.fg = white
c.colors.completion.item.selected.bg = blue
c.colors.completion.item.selected.border.bottom = c.colors.completion.category.border.top
c.colors.completion.item.selected.border.top = c.colors.completion.item.selected.bg
c.colors.completion.item.selected.fg = white
c.colors.completion.match.fg = pink
c.colors.completion.odd.bg = darkgrey
c.colors.contextmenu.disabled.bg = darkgrey
c.colors.contextmenu.disabled.fg = midgrey
c.colors.contextmenu.menu.bg =  darkgrey
c.colors.contextmenu.menu.fg =  white
c.colors.contextmenu.selected.bg = blue
c.colors.contextmenu.selected.fg = white
c.colors.downloads.bar.bg = black
c.colors.hints.bg = black
c.colors.hints.fg = blue
c.colors.hints.match.fg = white
c.colors.statusbar.insert.bg = blue
c.colors.tabs.bar.bg = black
c.colors.tabs.even.bg = midgrey
c.colors.tabs.even.fg = c.colors.tabs.odd.fg
c.colors.tabs.odd.bg = black
c.colors.tabs.odd.fg = white
c.colors.tabs.pinned.even.bg = black
c.colors.tabs.pinned.even.fg = blue
c.colors.tabs.pinned.odd.bg = midgrey
c.colors.tabs.pinned.odd.fg = blue
c.colors.tabs.pinned.selected.even.bg = blue
c.colors.tabs.pinned.selected.odd.bg = blue
c.colors.tabs.selected.even.bg = blue
c.colors.tabs.selected.odd.bg = blue
c.hints.border = black
#c.colors.webpage.bg = midgrey
