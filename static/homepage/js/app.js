const full = location.protocol + '//' + location.host;

let path = full + "/product/detail/"
function search(name) {
    $.ajax({
        url: `/product/search/${name}`,
        type: 'GET',
        success: function (response) {
            let div = document.createElement('div')
            div.setAttribute('class', 'position-absolute')
            div.setAttribute('style', 'top:50px')
            div.setAttribute('id', 'div_search')
            let parent = document.getElementById('content')
            parent.appendChild(div)
            for (let i = 0; i < response.length; i++) {
                let div_child = document.createElement('div')
                div_child.setAttribute('class', 'shadow p-3 bg-body rounded')
                let a = document.createElement('a');
                a.setAttribute('href', path + response[i].id + "/")
                a.setAttribute('class', 'text-decoration-none')
                a.innerHTML = response[i].title
                div_child.appendChild(a)
                div.appendChild(div_child);
            }
        }
    })
}
function myFunction() {
    let divs = document.getElementById('div_search')
    if (divs) {
        divs.remove()
    }
    let value = document.querySelector('#cowngu').value
    if (!value) {
        value = ' '
    }
    console.log(value)
    search(value)
}