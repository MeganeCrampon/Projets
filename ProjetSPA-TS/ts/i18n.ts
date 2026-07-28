function applyTranslations(language: Language): void {
    const langObj = translations[language] as unknown as Record<string, Record<string, any>>; // Cast to a more generic type for easier access
    const elements = document.querySelectorAll<HTMLElement>("[data-i18n]");

    elements.forEach((element) => {
        const key = element.dataset.i18n;
        if (!key) return;
        
        const pieces = key.split(".");
        const section = pieces[0];
        const field = pieces[1];

        const translation = langObj[section]?.[field];

        if (translation) {
            element.textContent = translation;
        }
    });

    const placeholderElements = document.querySelectorAll<HTMLInputElement>("[data-i18n-placeholder]");

    placeholderElements.forEach((element) => {
        const key = element.dataset.i18nPlaceholder;
        if (!key) return;

        const pieces = key.split(".");
        const section = pieces[0];
        const field = pieces[1];

        const translation = langObj[section]?.[field];

        if (translation) {
            element.placeholder = translation;
        }
    });

    const emptyTextElements = document.querySelectorAll<HTMLElement>("[data-i18n-empty]");

    emptyTextElements.forEach((element) => {
        const key = element.dataset.i18nEmpty;
        if (!key) return;   

        const pieces = key.split(".");
        const section = pieces[0];
        const field = pieces[1];

        const translation = langObj[section]?.[field];

        if (translation) {
            element.setAttribute("data-empty-text", translation);
        }
    });

    document.documentElement.lang = language; // met à jour l'attribut lang="fr"/"en" sur <html>
}