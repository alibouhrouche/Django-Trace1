(function () {
    const modalError = document.getElementById("modal-error")
    const modalConfirm = document.getElementById("modal-confirm")
    const desc = document.getElementById("modal-confirm_desc")
    const yes = document.getElementById("modal-confirm_yes")
    document.addEventListener("htmx:confirm", function(e) {
        if (
            e.detail.elt.getAttribute('hx-delete') === null &&
            e.detail.elt.getAttribute('hx-confirm') === null) return;
        e.preventDefault()
        console.log(e.detail)
        return new Promise(function (resolve, reject) {
            modalConfirm.checked = true
            desc.textContent = e.detail.question
            yes.onclick = function () {
                e.detail.issueRequest(true)?.then()
                modalConfirm.checked = false
            }
            modalConfirm.onchange = function () {
                resolve()
            }
        })
    })
    document.addEventListener("htmx:responseError", function(e) {
        modalError.checked = true
    })
})()
