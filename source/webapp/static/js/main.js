    async function buttonClick(event) {
        let target = event.target;
        let url = target.dataset['indexLink'];
        console.log(url)
        let response = await fetch(url);
        let index_text = await response.json();
        console.log(response)

    }
    async function onLoad(){
        const button = document.querySelectorAll(`[id="button"]`);
        if(button){
        for(let i of button){
            i.onclick = buttonClick
        }
        }
    }
    window.addEventListener('load', onLoad)