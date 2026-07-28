const languageSelector = document.getElementById("languageSelector") as HTMLSelectElement | null;

applyTranslations("fr"); // Applique les traductions par défaut (français) au chargement de la page

if (languageSelector) {
    languageSelector.addEventListener("change", () => {
        const selectedLanguage = languageSelector.value as Language;
        applyTranslations(selectedLanguage);
    });
}