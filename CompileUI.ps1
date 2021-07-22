$root = $(pwd)
cd ui_Files
$loc = $(pwd)
$fileList = (Get-ChildItem $loc)

#### COMPILE LOOP
foreach ($file in $fileList){
    $extn = [System.IO.Path]::GetExtension($file)
    if ($extn -eq ".ui"){
        $currentFile = $file | % {[System.IO.Path]::GetFileNameWithoutExtension($_)}
        $rawFile = $currentFile+".ui"
        $finalFile = "ui_"+$currentFile+".py"
        pyside2-uic $rawFile > $FinalFile
    }
    
    if ($extn -eq ".qrc"){
        $currentFile = $file | % {[System.IO.Path]::GetFileNameWithoutExtension($_)}
        $rawFile = $currentFile+".qrc"
        $finalFile = "rc_"+$currentFile+".py"
        pyside2-rcc $rawFile -o $FinalFile
    }
    
}
cd ..
#### 

#### MOVE LOOP
Move-Item -Path ui_Files\*.py -Destination .\
####
