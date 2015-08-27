__author__ = 'ysafe'

#
# DESC: song crawler to gather information from online sources
# BY: ysfdev
#
#


#REQUIRED MODULES

import subprocess as sp
import os, urllib, sys
from time import sleep
import shutil
import platform as pf
from functools import wraps

try:
    import wget, requests

except ImportError:

    print("Error Importing Wget and Requests packages. Packagess must be installed to start program")
    sleep(3)
    exit()


# PROMPT MENU FOR SONG OR ARTIST SEARCH
def song_search_prompt():

        musicCrawler.genre_search = "" # clear genre search
        print(30 * "*")
        print("*** SONG SEARCH ***")
        print(30 * "*")

        # Prompt user for artist to search
        song_search = str(input("Enter Artist or Song To Search or 0 (Go back): "))
        musicCrawler.search_string = song_search

        if song_search == '0':

            main()


# PROMPT MENU FOR GENRE SEARCH
def genre_search_prompt():

        musicCrawler.search_string = "" # clear song search variable
        print(30 * "*")
        print("*** GENRE SEARCH ***")
        print(30 * "*")

        print("Genres List:\n"
              "1)Hip Hop\n"
              "2)Latin Hip Hop\n"
              "3)R&B\n"
              "4)Reggae\n"
              "5)Reggaeton\n"
              "6)Dj Tools\n"
              "7)Dj Drops(Spanish)\n"
              "8)Bachata\n"
              "9)Tipico\n"
              "10)Merengue\n"
              "11)Salsa\n"
              "12)Cumbia\n"
              "13)Balada")

        print(30 * "-")
        genre_selection = str(input("Select Genre To Search or 0 (Go Back): "))

        if genre_selection == "1":

            genre_search = "Hip Hop"

        elif genre_selection == "2":

            genre_search = "Latin Hip Hop"

        elif genre_selection == "3":

            genre_search = "R%26B"

        elif genre_selection == "4":

            genre_search = "Reggae"

        elif genre_selection == "5":

            genre_search = "Reggaeton"

        elif genre_selection == "6":

            genre_search = "Dj Tools"

        elif genre_selection == "7":

            genre_search = "Drops"

        elif genre_selection == "8":

            genre_search = "Bachata"

        elif genre_selection == "9":

            genre_search = "Tipico"

        elif genre_selection == "10":

            genre_search = "Merengue"

        elif genre_selection == "11":

            genre_search = "Salsa"

        elif genre_selection == "12":

            genre_search = "Cumbia"

        elif genre_selection == "13":

            genre_search = "Balada"


        elif genre_selection == "0":

                main()

        else:
            print("Invalid Option")
            sleep(2)

        # Set search string to genre search
        musicCrawler.genre_search = genre_search

def download_options_prompt():

    print(30 * "*")
    header = "DOWNLOAD OPTIONS"
    print(header.center(30))
    print(30 * "*")

    print("Options Menu:\n"
          "1)Set Download Path\n"
          "2)Download Crawling Options")
    print(25 * "-")
    user_opt = str(input("Select option:( 0 to go back): "))

    if user_opt == '1':
        set_download_prompt()
    elif user_opt == '2':
        auto_crawling_mode_prompt()

def auto_crawling_mode_prompt():


        print("SELECT CRAWLING MODE:")
        print("1)Interactive mode\n"
              "2)Auto mode")

        opt = str(input("Enter Selection or (0 to go back): "))

        if opt == "1":

            musicCrawler.crawling_mode = 'interactive-mode'
            print(30 * "-")
            print("Interactive Crawling Mode Activated")


        elif opt == "2":
            musicCrawler.crawling_mode = 'auto-mode'
            print(30 * "-")
            print("Auto Crawling Mode Activated")

        elif opt == "0":
            download_options_prompt()
        else:
            print("Invalid Selection")

def set_download_prompt():

    global download_dir, download_path

    clear_shell_screen()

    print(30 * "*")
    print ("*** SETTING DOWNLOAD DIRECTORY ***")
    print(30 * "*")

    print("DIRECTORIES LOCATION:")
    print("1)OS Default Media Directory\n"
          "2)Another Location\n"
          "3)Print Current Download Path ")
    print(30 * "-")
    user_opt = str(input("Select Download Location( 0 to go back): "))

    if user_opt == '1':

        set_download_path()

        if not os.path.isdir(download_path):

         try:
            # open(download_path)
            print("Creating download directory")
            sleep(2)
            os.mkdir(download_path)


         except FileNotFoundError:
            print("OS Music dafault directory not found. Enter path manually")


        print("Download folder set to: ", download_path)
        sleep(2)


    elif user_opt == '2':

        dir_str = str(input("Enter Download Location: "))
        download_path = dir_str
        print("Download folder set to: ", download_path)
        sleep(2)



    elif user_opt == '3':

        print(download_path)

    elif user_opt == '0':
        download_options_prompt()

    else:
        print("Invalid Option. Enter Option From Menu")
        sleep(1)
        set_download_path()

    # set music crawler path to download_ path

    musicCrawler.download_dir = download_path

#CLEAR SCREEN OF SHELL

def clear_shell_screen():

    os_platform = pf.system()

    #check for the user OS platform to clear screen
    if os_platform == 'Linux':

        clear = sp.call('clear', shell=True)

    elif os_platform == "Windows":

        clear = sp.call('cls', shell=True)

    return clear

def set_download_path():

    os_platform = pf.system()
    user_path = os.path.expanduser("~")
    global download_path

    #check for the user OS to set download path
    download_path = os.path.join(user_path,  'Music', 'POOL_SONGS')

    #Set download directory with dowload path
    musicCrawler.download_dir = download_path


# DECORATOR FOR DOWNLOAD PATH

def verify_download_path_state(f):

    '''
    :param f: gets the set_download_env function to check is a directory has being created before starting download.
    :return: the
    '''

    @wraps(f) # wraps the given func with all its arguments
    def check_download_path(*args, **kwargs):
        user_path = os.path.expanduser("~")

        set_download_path()

        if musicCrawler.download_dir == "":

            print(20 * "#")
            print("A Download path must be created before starting download.")
            print(20 * "#")
            sleep(2)
            set_download_prompt()

        return f(*args, **kwargs)

    return check_download_path



# CLEAR SCREEN OF SHELL
def clear_shell_screen():

    os_platform = pf.system()

    # check for the user OS platform to clear screen
    if os_platform == 'Linux':

        clear = sp.call('clear', shell=True)

    elif os_platform == "Windows":

        clear = sp.call('cls', shell=True)

    return clear


# EXIT PROGRAM
def exit_program():

    clear_shell_screen()
    sys.exit()

# MAIN CLASS

class musicCrawler:

    #CLASS VARIABLES
    download_dir = ""
    page_num = 1
    last_page = 0
    search_string = ""
    genre_search = ""
    crawling_mode = "interactive-mode"  # defines default crawling mode

    # Paste music source URls list below this line
    song_url = ""  # song download url goes here. Gets songs by name and artist
    song_page_count_url = ""  # get the totals number of songs pages

    genre_url = ""  # genre download url goes here. Gets songs by Genre search
    genre_page_count_url = ""  # get the total of genre pages

    music_download_url = ""  # contains songs mp3 files.

    # GET MUSIC DATA
    def get_music_data(self, search_option):
        """
        :param search_option: Sets the option for the URL to be used either 'song' or 'genre'.
        :return: Display retrieved songs list
        """

        if musicCrawler.song_url == "" or musicCrawler.genre_url == "":

            print("Download sources not provided. Check Readme for details.")
            sleep(3)
            main()

        else:
            string_search = musicCrawler.search_string.upper()
            q = {'keywords': string_search}
            search_query = str(urllib.parse.urlencode(q))
            genre_search = str(musicCrawler.genre_search)
            page_num = str(musicCrawler.page_num)

            if search_option == 'song':

                data_url = musicCrawler.song_url % (page_num, search_query)
                last_page_count_url = musicCrawler.song_page_count_url % search_query

            elif search_option == 'genre':
                data_url = musicCrawler.genre_url % (page_num, genre_search)
                last_page_count_url = musicCrawler.genre_page_count_url % genre_search

            # GET data from url
            try:
                print("retrieving data ...")
                response_data = requests.get(data_url)
                response_last_page_count = requests.get(last_page_count_url)
            except Exception:
                print("Error retrieving data from source.")

            if response_data.status_code == 200:

                # Decode the Json response into  a dict
                music_data = response_data.json()
                total_pages_count = response_last_page_count.json()

                # parse data and display it
                musicCrawler.parse_music_data(self, music_data, total_pages_count)

            else:

                print("Unable To Parse Data.")

    # GET & DISPLAY SONGS
    def parse_music_data(self, music_data, total_pages_count):

            clear_shell_screen()  # clear screen

            # Total Records Found
            total_records = str(music_data['totalRecords'])

            # Setting Page Count
            last_page_count = str(total_pages_count['count'])

            # Total Records in music_data
            musicCrawler.music_data_count = str(len(music_data['data']))

            counter = 0

            song_search = musicCrawler.search_string.upper()
            genre_search = musicCrawler.genre_search.upper()
            search = song_search if genre_search == "" else genre_search
            page_num = int(musicCrawler.page_num)


            print(30 * "*")
            print("*** SONG CRAWLER ***")
            print(30 * "*")
            print("LOADING -" + search + "- SEARCH ...")
            sleep(3)

            clear_shell_screen()
            print(30 * "-")
            print("### FOUND " + total_records + " RECORDS AND " + last_page_count + " PAGES ###")
            print(30 * "-")

            print("*** SONGS LIST ***")

            # iterating over dict to get song info
            for songs in music_data['data']:

                #You can enable any options below to get more information from song files

                # album_name = music_data['data'][counter]['aAlbum']
                #artist_name = music_data['data'][counter]['Artist']
                # date_added = music_data['data'][counter]['DateAdded']
                # song_genre = music_data['data'][counter]['aGenre']
                # song_ID = music_data['data'][counter]['audioId']  # convert to int before using
                # song_title = music_data['data'][counter]['aTitle']
                # song_duration = music_data['data'][counter]['aDuration']
                song_bmp = music_data['data'][counter]['aBpm']  # must be converted to int before print
                song_year = music_data['data'][counter]['aYear']
                song_file_name = music_data['data'][counter]['aFile']  # Has .mp3 file


                print("[" + str(counter) + "] - ", song_file_name) # "BMP:", song_bmp, "YEAR:", song_year)

                if counter < 100:  # Making sure not to iterate past the last song

                    counter += 1


                print(30 * "-")

            if musicCrawler.crawling_mode == 'interactive-mode':

                download_option = str(input("Download Songs On This List ? (y or n): "))

                if download_option == "y":

                    musicCrawler.set_download_env(self, search, music_data, page_num, last_page_count)


                elif download_option == "n":
                    opt = str(input("Page " + str(page_num) + " of " + str(last_page_count) + " | Go To Next Page? (y or n): "))

                    if opt == 'y':
                        musicCrawler.load_next_page(self, page_num, last_page_count)

                    elif opt == 'n':
                        main()

                    else:
                        print("Invalid Option")

            elif musicCrawler.crawling_mode == 'auto-mode':

                musicCrawler.auto_crawler_mode(self, search, music_data, last_page_count, page_num )


    def auto_crawler_mode(self, search, music_data, last_page_count, page_num):

        clear_shell_screen()
        print(30 * "*")
        print("AUTO CRAWLING MODE")
        print(30 * "*")
        # start download envionment
        musicCrawler.set_download_env(self, search, music_data, page_num, last_page_count)


    # LOAD NEXT PAGE
    def load_next_page(self, page_num, last_page_count):

        if page_num != int(last_page_count):

            print("LOADING PAGE "+page_num+" ""... ")

            # if musicCrawler.page_num != musicCrawler.last_page:

            musicCrawler.page_num += 1

            if musicCrawler.genre_search != "":

                musicCrawler.get_music_data(self, 'genre')

            if musicCrawler.search_string != "":

                musicCrawler.get_music_data(self, 'song')
        else:
            print("No more pages to crawl")
            sleep(2)
            main()

    # SETUP DOWNLOAD ENVIRONMENT
    @verify_download_path_state
    def set_download_env(self, search_string, music_data, page_num, last_page_count):
        #os.path.defpath(musicCrawler.download_dir, search_string)
        download_dir = musicCrawler.download_dir + "/" + search_string
        search_string = search_string.replace(" ", "_")

        if not (os.path.exists(download_dir)):
            print("Creating Directory: " + search_string)
            os.mkdir(download_dir)
            os.chdir(download_dir)
        else:
            os.chdir(download_dir)

        counter = 0

        print("*** DOWNLOADING ***")

        for songs in music_data['data']:

            # getting audioID  and the file name from song required for download
            song_ID = music_data['data'][counter]['audioId']
            song_file_name = music_data['data'][counter]['aFile']

            if not os.path.isfile(os.path.join(download_dir, song_file_name)): # check if song has been downloaded before

                musicCrawler.download_song(self, song_file_name, int(song_ID), download_dir)

            else:
                print("Skipping song "+song_file_name+". Already downloaded ")

            if counter < 100:  # Making sure not to iterate past the last song

                counter += 1

        print(30 * "-")
        print("---- PAGE "+str(page_num)+" DOWNLOAD COMPLETED -----")

        if musicCrawler.crawling_mode == 'interactive-mode':

            opt = str(input("Page "+str(page_num)+" of "+str(last_page_count)+" | Go To Next Page? (y or n): "))

            if opt == 'y':

                musicCrawler.load_next_page(self, page_num, last_page_count)

            else:
                main()

        elif musicCrawler.crawling_mode == 'auto-mode':

            musicCrawler.load_next_page(self, page_num, last_page_count)


    # DOWNLOAD SONGS
    def download_song(self, songTitle, song_ID, download_dir):

        song_ID = str(song_ID)
        download_url = (musicCrawler.music_download_url + song_ID + ".mp3")
        song_local_path = os.path.join(download_dir, songTitle)

        print(30 * "-")
        print("Downloading Song: " + songTitle)

        # handle exception if mp3 file is not found on url source

        try:
            wget.download(download_url, download_dir)  # download the mp3 file from url to download directory

        except Exception:
            print("Song ", songTitle + " Not Found")
            pass

        # join the song Id  with the download dir to get the song tittle path
        song_ID = (song_ID+".mp3")
        song_ID_path = os.path.join(download_dir, song_ID)
        song_title_path = os.path.join(download_dir, songTitle)

        try:
            print("\n""Parsing Song: " + songTitle)
            shutil.move(song_ID_path, song_title_path)  # parse the song id with actual song name
            print(30 * "-")
        except FileNotFoundError:
            print("Song ID ", song_ID + " Not Found")
            pass


# MAIN FUNCTION
def main():

    #Clear Shell Screen
    clear_shell_screen()

    #Start Crawler
    crawler = musicCrawler()

    while True:

        clear_shell_screen()
        print(30 * '*')
        header = "YSF SONG DOWNLOADER"
        print(header.center(30))
        print(30 * '*')
        print("SELECT OPTION MENU:\n"
              "------------------------\n"
              "1)Search Artist or Song\n"
              "2)Search By Genre\n"
              "3)Search Zip Files\n"
              "4)Download Options\n"
              "5)Exit")

        print(23 * "-")
        try:

            opt = str(input("SELECT OPTION: "))

            if opt == '1':
                clear_shell_screen()
                song_search_prompt()
                crawler.get_music_data('song')

            elif opt == '2':
                clear_shell_screen()
                genre_search_prompt()
                crawler.get_music_data('genre')

            elif opt == '3':
                clear_shell_screen()
                print("Zip Files Mode Coming Soon")
                sleep(2)

            elif opt == '4':
                clear_shell_screen()
                download_options_prompt()
                sleep(2)

            elif opt == '5':

                print("Exiting...")
                sleep(1)
                # exit_program(br)
                crawler.exit_program()
                break
            else:
                print(20 * "-")
                print("Invalid Option. Try Again")
                sleep(2)

        except ValueError:
            print("Error: is not a valid number ")
            sleep(2)


# MAIN PROGRAM START
if __name__ == '__main__':

    try:
        main()

    except KeyboardInterrupt:
        pass



