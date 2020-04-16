# py-wearmodder
WearModder (WearOS tool) ported to Python.

Full credit to [**moneytoo** from XDADevelopers](https://forum.xda-developers.com/wear-os/development/app-spotify-lite-scaled-standalone-wear-t3815680) for the idea and original Java code for this.

I simply ported it to Python, as I had some issues with the original version when trying to convert other apps.

# Full instructions (modified slightly from original thread):

## Decompile apk
java -jar apktool_2.3.3.jar d spotify-lite.apk

## Mod resources (use directory)
python ./wearmodder.py ./spotify-lite/res

## Perform additional manual tweaks

## Build apk
java -jar apktool_2.3.3.jar b spotify-lite

## Sign
keytool -genkey -v -keystore my-release-key.keystore -alias alias_name -keyalg RSA -keysize 2048 -validity 10000

jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore my-release-key.keystore spotify-lite/dist/spotify-lite.apk alias_name
