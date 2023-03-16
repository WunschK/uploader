console.log('hello world from main.js')
Dropzone.autoDiscover = false;
    const myDropzone = new Dropzone("#my-dropzone",
    {
        url: 'dz_upload/',
        maxFiles:3,
        maxFilesize: 2,
        acceptedFiles: '.jpg',
        dictDefaultMessage:'whoop'
    })





