#! /bin/sh

echo “Do you want to open Chrome in Kiosk mode?”
echo “Type Y to proceed and N to exit”
read ans
if [ “$ans” = “Y” ]; then
    echo “Opening Chrome in Kiosk Mode”
    chromium-browser –kiosk –noerrdialogs
elif [ “$ans” = “N” ]; then
    echo “Script Terminated!”
else
    echo “Enter valid input.”
fi