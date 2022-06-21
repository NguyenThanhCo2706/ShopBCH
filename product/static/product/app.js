a = document.getElementsByClassName('price-product')
for (let i = 0; i < a.length; i++) {
    var x = Number(a[i].innerHTML)
    x = x.toLocaleString('it-IT', { style: 'currency', currency: 'VND' });
    a[i].innerHTML = x
}