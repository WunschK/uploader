console.log("hi there")

function dropHandler(ev) {
    console.log("File(s) dropped");
    // Prevent default behavior (Prevent file from being opened)
    ev.preventDefault();

    if (ev.dataTransfer.items) {
        [...ev.dataTransfer.items].forEach((item, i) => {
            if (item.kind === 'file') {
                const file = item.getAsFile();
                // file handling and actual uploading to the media directory will be done here
    } else {
        // Use DataTransfer interface to access the file(s)
        [...ev.dataTransfer.files].forEach((file, i) => {
            console.log(`… file[${i}].name = ${file.name}`);
        });
    }
}


function dragOverHandler(ev){
    console.log('dragging over');
    ev.preventDefault();
}