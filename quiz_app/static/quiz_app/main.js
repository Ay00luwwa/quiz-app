function checkAnswers() {
    let score = 0;
    const q1 = document.querySelector('input[name="q1"]:checked').value;

    if (q1 === "Paris") {
        score++;
    }

    document.getElementById('result').innerText = "You scored: " + score + "/1";
}
