function ConnectButton(){
    console.log("Connect pushed"); 
    document.querySelector("#top-toolbar > colab-connect-button").shadowRoot.querySelector("#connect").click() 
}
setInterval(ConnectButton,60000);

//https://colab.research.google.com/drive/1LPiMkWQNQcj7X61d62NkgNZdg_rZiVJr#scrollTo=TE5_izRlYtrP
//https://stackoverflow.com/questions/71456390/how-to-keep-the-google-colab-running-without-disconnecting-in-2022
