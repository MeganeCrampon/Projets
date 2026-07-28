(function () {

    const form = document.getElementById("compatibilityForm") as HTMLFormElement | null;
    const name1Input = document.getElementById("name1") as HTMLInputElement | null;
    const name2Input = document.getElementById("name2") as HTMLInputElement | null;
    const result = document.getElementById("compatibilityResult") as HTMLElement | null;
    const languageSelector = document.getElementById("languageSelector") as HTMLSelectElement | null;


    if (!form || !name1Input || !name2Input || !result || !languageSelector) {
        return;
    }

    // les emojis, dans le même ordre que les tranches (index 0 à 11)
    const fireworkEmojis = [
        "💀", "😬", "🥺", "😅", "🙃", "🙂", "😉", "😊", "😇", "🥰", "😍", "💖"
    ];

    function capitalize(word: string) {
        return word.charAt(0).toUpperCase() + word.slice(1);
    }

    function launchFireworks(emoji: string) {
        const fireworksDiv = document.createElement('div');
        fireworksDiv.classList.add('emoji-burst');
        document.body.appendChild(fireworksDiv);

        const rect1 = name1Input.getBoundingClientRect();
        const rect2 = name2Input.getBoundingClientRect();
        const centerX = (rect1.left + rect1.right + rect2.left + rect2.right) / 4;
        const centerY = Math.min(rect1.top, rect2.top) - 20;

        for (let i = 0; i < 60; i++) {
            const emojiParticle = document.createElement('span');
            emojiParticle.textContent = emoji;
            emojiParticle.classList.add('emoji-particle');

            emojiParticle.style.left = `${centerX}px`;
            emojiParticle.style.top = `${centerY}px`;

            const angle = Math.random() * 2 * Math.PI;
            const distance = 250 + Math.random() * 300;

            const tx = Math.cos(angle) * distance;
            const ty = Math.sin(angle) * distance;

            emojiParticle.style.setProperty("--tx-end", `${tx}px`);
            emojiParticle.style.setProperty("--ty-end", `${ty}px`);
            emojiParticle.style.setProperty("--tx-start", `${tx * 0.3}px`);
            emojiParticle.style.setProperty("--ty-start", `${ty * 0.3}px`);
            emojiParticle.style.setProperty("--rot-start", `${Math.random() * 360}deg`);
            emojiParticle.style.setProperty("--rot-end", `${Math.random() * 720 - 360}deg`);

            fireworksDiv.appendChild(emojiParticle);
        }

        setTimeout(() => {
            fireworksDiv.remove();
        }, 1700);
    }

    form.addEventListener('submit', (event: SubmitEvent) => {
        event.preventDefault();

        const name1: string = name1Input.value.trim().toLowerCase();
        const name2: string = name2Input.value.trim().toLowerCase();
        const names: string[] = [name1, name2].sort();
        const combinaison: string = names[0] + names[1];

        let lettersSum: number = 0;
        for (let l = 0; l < combinaison.length; l++) {
            lettersSum += combinaison.charCodeAt(l);
        }

        const percentage: number = lettersSum % 101;

        let messageIndex: number;

        if (percentage === 0) {
            messageIndex = 0;
        } else if (percentage < 10) {
            messageIndex = 1;
        } else if (percentage < 20) {
            messageIndex = 2;
        } else if (percentage < 30) {
            messageIndex = 3;
        } else if (percentage < 40) {
            messageIndex = 4;
        } else if (percentage < 50) {
            messageIndex = 5;
        } else if (percentage < 60) {
            messageIndex = 6;
        } else if (percentage < 70) {
            messageIndex = 7;
        } else if (percentage < 80) {
            messageIndex = 8;
        } else if (percentage < 90) {
            messageIndex = 9;
        } else if (percentage < 100) {
            messageIndex = 10;
        } else {
            messageIndex = 11;
        }

        const currentLanguage: string = languageSelector.value;
        const compatibilityTranslations = translations[currentLanguage].compatibility;

        const message: string = compatibilityTranslations.messages[messageIndex];
        const emoji: string = fireworkEmojis[messageIndex];

        launchFireworks(emoji);

        result.textContent = compatibilityTranslations.resultText
            .replace("{name1}", capitalize(name1))
            .replace("{name2}", capitalize(name2))
            .replace("{percentage}", percentage)
            .replace("{message}", message);
    });

})();