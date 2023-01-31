    async function buttonClick(event) {
        let target = event.target;
        let url = target.dataset['indexLink'];
        let response = await fetch(url);
        let index_text = await response.json();
        let count = document.getElementById('value'+index_text.pk)
        count.innerText = 'Лайки: '+ index_text.like
        let icon = document.getElementById('icon'+index_text.pk)

        if(index_text.result ===0){
            icon.innerHTML = `<i class="bi bi-hand-thumbs-up"></i>`
        }
        else {
            icon.innerHTML = `<i class="bi bi-hand-thumbs-up-fill"></i>`
        }
    }
    async function onLoad(){
        const button = document.querySelectorAll(`[id="button"]`);
        if(button){
        for(let i of button){
            i.onclick = buttonClick;
        }
        }
    }
    window.addEventListener('load', onLoad);