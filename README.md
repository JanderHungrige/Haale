**-----Gesichtserkennung und Zählung-----**

**--Vorbereiten:**

**Installieren von Conda**

Ich würde Ihnen raten Anaconda zu installieren

Ubuntu:

`apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2
libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6`

Ansonsten hier mal nachsehen:
https://docs.anaconda.com/anaconda/install/linux/

**Erstelle Enviroment**

Folgend können Sie eine enviroment aufsetzten mittels der *.yml Datei (Für Conda Nutzer). Die Python module werden mit der *.txt Datei erstellt Die enviroment enthält dann allen benötigten Modulen.

Erstelle die enviroment mittles der **yml Datei** (Conda Nutzer). Die erste Zeiel ist der enviroment name. Kann natürlich vorher geändert werden:

`conda env create -f environment.yml`

Oder der der **txt datei** (conda oder pip user):

conda: `conda create --name <env_name> --file <.txt file>`

pip: `pip install -r requirements.txt`


Die enviroment kann man im terminal(linux) oder conda-terminal(windows) 
mit:
`conda activate <enviromentname>`
aktivieren. Dann sollte der Code sofort funktionieren. Sie können den
code zum bearbeiten z.B. mit *Spyder* öffnen (ist mit installiert).


**--Erläuterung Dateien:**
> MTCNN.py 

 pyhton code der den MTCNN classifier verwendet um Gesichter zuverlässig zu erkennen.
 Erkannte gesicher werden gezält und der Mittlewert ausgegeben.
 Der video output kann in * Zeile 22 * mit True oder False an oder ausgestellt werden (speedup)
 
  > mtcnn-env.yml
  
   Mit dieser Datein kann eine Conda enviroment erstellt werden. Alle Module sollten enthalten sein. 
 
 > requirements.txt
 
   Hier stehen alle benötigten module um mit pip oder conda installiert zu werden. Wie oben beschrieben lässt sich damit eine enviroment erstellen, die alle module installiert.
 

