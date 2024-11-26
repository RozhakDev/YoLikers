try:
    import requests, json, time, re, urllib.parse, os, sys
    from rich import print as printf
    from rich.console import Console
    from rich.panel import Panel
    from requests.exceptions import RequestException
except (ModuleNotFoundError) as e:
    exit(f"Error: {str(e).capitalize()}!")

def TAMPILKAN_LOGO():
    os.system('cls' if os.name == 'nt' else 'clear')
    printf(Panel(r"""[bold red]   _     _          _       _ _                     
  | |   | |        (_)     (_) |                    
  | |___| | ___     _       _| |  _ _____  ____ ___ 
  |_____  |/ _ \   | |     | | |_/ ) ___ |/ ___)___)
   _____| | |_| |  | |_____| |  _ (| ____| |  |___ |
[bold white]  (_______|\___/   |_______)_|_| \_)_____)_|  (___/ 
        [underline green]Free Facebook Likes - Coded by Rozhak""", width=59, style="bold bright_black"))

def HEADERS():
    return (
        {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Host': 'app.pagalworld2.com',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 9; RMX3301 Build/PQ3A.190605.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Safari/537.36',
            'v': '3.9', # CHANGE TO THE LATEST VERSION!
            'X-Requested-With': 'com.yo.app'
        }
    )

SUKSES, COOKIES, GAGAL, LOOPING = [], {
    "KEY": None
}, [], 0

class MAIN:

    def __init__(self) -> None:
        pass

    def LOGIN_COOKIES(self):
        try:
            TAMPILKAN_LOGO()
            printf(Panel(f"[bold white]Please fill in your Facebook cookies, make sure to use a new account to login, we\ndo not recommend using a real account!", width=59, style="bold bright_black", subtitle="[bold bright_black][bold bright_black]╭──────", subtitle_align="left", title="[bold bright_black][Cookies Facebook]"))
            self.COOKIES = Console().input("[bold bright_black]   ╰─> ")
            if 'c_user=' in str(self.COOKIES):
                printf(Panel(f"[bold white]Please fill in the post id you want to react to, make sure the post can be liked by the\npublic and is not private. Fill in only numbers!", width=59, style="bold bright_black", subtitle="[bold bright_black][bold bright_black]╭──────", subtitle_align="left", title="[bold bright_black][ID Postingan]"))
                self.POST_ID = int(Console().input("[bold bright_black]   ╰─> "))
                printf(Panel(f"[bold white]Please fill in the type of reaction you want from `[bold green]LIKE, LOVE, CARE, HAHA, WOW, SAD, and ANGRY[bold white]`, you can only enter one, no more. For example:[bold green] HAHA", width=59, style="bold bright_black", subtitle="[bold bright_black][bold bright_black]╭──────", subtitle_align="left", title="[bold bright_black][Tipe Reaksi]"))
                self.TIPE_REACTION = Console().input("[bold bright_black]   ╰─> ")
                if self.TIPE_REACTION in ['LIKE', 'LOVE', 'CARE', 'HAHA', 'WOW', 'SAD', 'ANGRY']:
                    printf(Panel(f"[bold white]You can use[bold yellow] CTRL + C[bold white] if stuck and[bold red] CTRL + Z[bold white] if you want to stop, *remember if\nlogin fails please change your Facebook!", width=59, style="bold bright_black", title="[bold bright_black][Catatan]"))
                    time.sleep(2.5)
                    while True:
                        try:
                            if COOKIES['KEY'] == None:
                                printf(f"[bold bright_black]   ──>[bold green] CHECKING YOUR COOKIES!          ", end='\r')
                                time.sleep(2.5)
                                self.VALIDASI_COOKIES(facebook_cookies=self.COOKIES)
                                continue
                            else:
                                printf(f"[bold bright_black]   ──>[bold green] SENDING REACTION!               ", end='\r')
                                time.sleep(2.5)
                                self.KIRIMKAN_REAKSI(post_id=self.POST_ID, tipe_rections=self.TIPE_REACTION)
                                continue
                        except (RequestException):
                            printf(f"[bold bright_black]   ──>[bold red] YOUR CONNECTION IS HAVING A PROBLEM!     ", end='\r')
                            time.sleep(10.5)
                            continue
                        except (KeyboardInterrupt):
                            printf(f"                                   ", end='\r')
                            time.sleep(4.5)
                            continue
                        except (Exception) as e:
                            printf(f"[bold bright_black]   ──>[bold red] {str(e).upper()}!   ", end='\r')
                            time.sleep(10.5)
                            continue
                else:
                    printf(Panel(f"[bold red]You must fill in the reaction type according to the choices above, and please choose only one, no\nmore, and make sure there are no spelling mistakes!", width=59, style="bold bright_black", title="[bold bright_black][Reaksi Salah]"))
                    sys.exit()
            else:
                printf(Panel(f"[bold red]The cookies you entered are incorrect, please enter the cookies correctly,\nyou can use Via Browser to get cookies!", width=59, style="bold bright_black", title="[bold bright_black][Cookies Salah]"))
                sys.exit()
        except (Exception) as e:
            printf(Panel(f"[bold red]{str(e).capitalize()}!", width=59, style="bold bright_black", title="[bold bright_black][Error]"))
            sys.exit()

    def VALIDASI_COOKIES(self, facebook_cookies):
        with requests.Session() as session:
            session.headers.update(
                HEADERS()
            )
            response = session.get('https://app.pagalworld2.com/')
            self.COOKIES_STRING = "; ".join([str(key) + "=" + str(value) for key, value in session.cookies.get_dict().items()])
            session.headers.update(
                {
                    'Cookie': '{}'.format(self.COOKIES_STRING)
                }
            )
            params = {
                'cookie': '{}'.format(facebook_cookies),
                'access_token': '',
            }
            response2 = session.get('https://app.pagalworld2.com/login.php', params=params)
            if 'Login%20Successful' in str(response2.url):
                COOKIES.update(
                    {
                        "KEY": "; ".join([str(key) + "=" + str(value) for key, value in session.cookies.get_dict().items()])
                    }
                )
                printf(f"[bold bright_black]   ──>[bold green] LOGIN SUCCESSFUL!              ", end='\r')
                time.sleep(3.5)
                return (True)
            elif 'Session%20Expired%20Login%20Again.' in str(response2.url):
                printf(Panel(f"[bold red]The cookies you entered seem to have expired or your account has been hit by a checkpoint!", width=59, style="bold bright_black", title="[bold bright_black][Login Gagal]"))
                sys.exit()
            elif 'Your Account is locked kindly clear Checkpoint and Login Again.' in str(response2.text):
                printf(Panel(f"[bold red]Your account has been locked, please clear the checkpoint and try again!", width=59, style="bold bright_black", title="[bold bright_black][Login Gagal]"))
                sys.exit()
            elif 'Please Upload Profile Pic and Login Again' in str(response2.text):
                printf(Panel(f"[bold red]Your account has not uploaded a profile picture, please upload a profile picture and try again!", width=59, style="bold bright_black", title="[bold bright_black][Login Gagal]"))
                sys.exit()
            else:
                printf(Panel(f"[bold red]Our system encountered an unexpected error while logging in to Yolikers,\nplease make sure your cookies are correct!", width=59, style="bold bright_black", title="[bold bright_black][Login Error]"))
                sys.exit()

    def KIRIMKAN_REAKSI(self, post_id, tipe_rections):
        global SUKSES, GAGAL, LOOPING
        with requests.Session() as session:
            session.headers.update(
                HEADERS()
            )
            session.headers.update(
                {
                    'Cookie': '{}'.format(COOKIES['KEY'])
                }
            )
            response = session.get('https://app.pagalworld2.com/dashboard.php?type=custom')
            if 'index.php?error=Login' in str(response.url):
                printf(f"[bold bright_black]   ──>[bold green] YOUR COOKIES HAVE EXPIRED!  ", end='\r')
                COOKIES.update({
                    "KEY": None
                })
                time.sleep(4.5)
                return (False)
            elif 'Time Limit Reached' in str(response.text):
                printf(Panel(f"[bold red]You have exceeded today's limit, please try again tomorrow or use another account, because\neach account can only send reactions 10 times!", width=59, style="bold bright_black", title="[bold bright_black][Reaksi Limit]"))
                sys.exit()
            else:
                self.FIND_KEY_VALUE = re.search(r'type="hidden" name="([^"]*)"[^>]*value="([^"]*)"', str(response.text))
                self.KEY, self.VALUE = self.FIND_KEY_VALUE.group(1), self.FIND_KEY_VALUE.group(2)
                self.KEY_ID_POST = re.search(r'name="([^"]*)"[^>]*placeholder=', str(response.text)).group(1)
                self.SUBMIT = re.search(r'type="submit"[^>]*name="([^"]*)"', str(response.text)).group(1)
                self.DATA_SITEKEY = re.search(r'data-sitekey="(.*?)"', str(response.text)).group(1)

                data = {
                    f'{self.KEY_ID_POST}': '{}'.format(post_id),
                    'type': '{}'.format(tipe_rections), # LIKE, LOVE, CARE, HAHA, WOW, SAD, ANGRY
                    f'{self.KEY}': f'{self.VALUE}',
                    'g-recaptcha-response': f'{BYPASS().reCAPTCHA(self.DATA_SITEKEY)}',
                    f'{self.SUBMIT}': 'Submit',
                }

                session.headers.update(
                    {
                        'Referer': 'https://app.pagalworld2.com/dashboard.php?type=custom',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Content-Length': '{}'.format(len(urllib.parse.urlencode(data))),
                        'Origin': 'https://app.pagalworld2.com',
                    }
                )
                response2 = session.post('https://app.pagalworld2.com/dashboard.php?type=custom', data=data)
                LOOPING += 1
                if '/?i=' in str(response2.url) and 'Likes Send' in str(response2.url) or 'Likes%20Send' in str(response2.url):
                    try:
                        self.JUMLAH_REAKSI = re.search(r'/\?i=(\d+)', str(response2.url)).group(1)
                    except (AttributeError):
                        self.JUMLAH_REAKSI = ('null')
                    printf(f"[bold bright_black]   ──>[bold green] SUCCESSFULLY SENDING REACTION!  ", end='\r')
                    time.sleep(4.5)
                    SUKSES.append(f'{response2.url}')
                    printf(Panel(f"""[bold white]Status :[italic green] Successfully sent likes...[/]
[bold white]Link :[bold red] https://www.facebook.com/{post_id}
[bold white]Reaksi :[bold yellow] +{self.JUMLAH_REAKSI}""", width=59, style="bold bright_black", title="[bold bright_black][Sukses]"))
                    for sleep in range(900, 0, -1):
                        time.sleep(1.0)
                        printf(f"[bold bright_black]   ──>[bold white] TUNGGU[bold green] {sleep}[bold white]/[bold red]{post_id}[bold white]/[bold green]{LOOPING}[bold white] SUKSES:-[bold green]{len(SUKSES)}[bold white] GAGAL:-[bold red]{len(GAGAL)}[bold white]     ", end='\r')
                    return (True)
                elif 'dashboard.php?type=custom' in str(response2.url):
                    GAGAL.append(f'{response2.url}')
                    printf(f"[bold bright_black]   ──>[bold red] WRONG POST ID!                  ", end='\r')
                    time.sleep(4.5)
                    return (False)
                else:
                    GAGAL.append(f'{response2.url}')
                    printf(f"[bold bright_black]   ──>[bold red] ERROR WHILE SENDING REACTION!   ", end='\r')
                    time.sleep(5.5)
                    return (False)

class BYPASS:

    def __init__(self) -> None:
        pass

    def reCAPTCHA(self, sitekey):
        with requests.Session() as r:
            self.KEY = json.loads(open('Penyimpanan/Key.json', 'r').read())['LICENSE'] # PLEASE CHANGE IT WITH THE KEY YOU HAVE!
            response = r.get(f'http://api.multibot.in/in.php?key={self.KEY}&method=userrecaptcha&googlekey={sitekey}&pageurl=https://app.pagalworld2.com/dashboard.php?type=custom')
            if 'ERROR_ZERO_BALANCE' not in str(response.text):
                self.STATUS, self.ID = str(response.text).split('|')[0], str(response.text).split('|')[1]
                if 'OK' in str(response.text):
                    while True:
                        response2 = requests.get(f'http://api.multibot.in/res.php?key={self.KEY}&id={self.ID}')
                        if 'OK|' in str(response2.text):
                            printf(f"[bold bright_black]   ──>[bold green] SUCCESSFULLY BYPASS CAPTCHA!             ", end='\r')
                            time.sleep(1.5)
                            return (str(response2.text).split('|')[1])
                        elif 'CAPCHA_NOT_READY' in str(response2.text):
                            for sleep in range(60, 0, -1):
                                time.sleep(1.0)
                                printf(f"[bold bright_black]   ──>[bold white] TUNGGU[bold green] {sleep}[bold white] DETIK                           ", end='\r')
                            continue
                        else:
                            printf(f"[bold bright_black]   ──>[bold yellow] TRY BYPASS CAPTCHA!                  ", end='\r')
                            time.sleep(1.5)
                            self.reCAPTCHA(sitekey)
                else:
                    printf(f"[bold bright_black]   ──>[bold red] CAPTCHA NOT FOUND!                  ", end='\r')
                    time.sleep(3.5)
                    self.reCAPTCHA(sitekey)
            else:
                printf(Panel(f"[bold red]The credit in your multibot account has run out, please try using another account, make sure you\nhave enough credit and make sure the key is correct!", width=59, style="bold bright_black", title="[bold bright_black][Kredit Habis]"))
                sys.exit()

if __name__ == '__main__':
    try:
        if os.path.exists("Penyimpanan/Subscribe.json") == False:
            youtube_url = json.loads(requests.get('https://raw.githubusercontent.com/RozhakXD/YoLikers/refs/heads/main/Penyimpanan/Youtube.json').text)['Link']
            os.system(f'xdg-open {youtube_url}')
            with open('Penyimpanan/Subscribe.json', 'w') as w:
                w.write(
                    json.dumps(
                        {
                            "Status": True
                        }
                    )
                )
            w.close()
            time.sleep(2.5)
        os.system('git pull')
        MAIN().LOGIN_COOKIES()
    except (Exception) as e:
        printf(Panel(f"[bold red]{str(e).capitalize()}!", width=59, style="bold bright_black", title="[bold bright_black][Error]"))
        sys.exit()
    except (KeyboardInterrupt):
        sys.exit()