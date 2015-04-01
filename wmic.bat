for /F %%i in (ip.txt) do 

(

echo Processing %%i...

wmic /Failfast:ON /node:"%%i" OS Get csname,name

wmic /Failfast:ON /node:"%%i" bios Get serialnumber

)

PAUSE