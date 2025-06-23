let arrList = [];
const btn1 = document.getElementById("btn1");
const inp = document.getElementById("inp");
const boxContainer = document.getElementsByClassName("boxContainer")[0];
const btnReset1 = document.getElementById("btnReset1");

btnReset1.onclick = () => {
    boxContainer.innerHTML = "";
    // arrList = [];
}

btn1.onclick = () => {
    const value = inp.value;
    arrList.push(value);

    boxContainer.innerHTML = ""

    arrList.forEach((item, index) => {
        const div = document.createElement("div");
        div.textContent = item;
        boxContainer.append(div);
    })
}