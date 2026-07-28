(function () {
    const plushieForm = document.getElementById("plushieForm") as HTMLFormElement | null;
    const currency = document.getElementById("currency") as HTMLSelectElement | null;
    const plushieName = document.getElementById("name") as HTMLInputElement | null;
    const hours = document.getElementById("hours") as HTMLInputElement | null;
    const minutes = document.getElementById("minutes") as HTMLInputElement | null;
    const materialPrice = document.getElementById("materialPrice") as HTMLInputElement | null;
    const patternPrice = document.getElementById("patternPrice") as HTMLInputElement | null;
    const priceResult = document.getElementById("priceResult") as HTMLDivElement | null;

    type Currency = "EUR" | "USD" | "GBP";

    const convertionRate: Record<Currency, number> = {
    EUR: 1,
    USD: 1.08,
    GBP: 0.85
    };

    const currencySymbol: Record<Currency, string> = {
    EUR: '€',
    USD: '$',
    GBP: '£'
    };

    if (!plushieForm || !currency || !plushieName || !hours || !minutes || !materialPrice || !patternPrice || !priceResult) {
        return;
    }

    plushieForm.addEventListener('submit', (event: SubmitEvent) => {
        event.preventDefault();

        const totalHours: number = Number(hours.value) + (Number(minutes.value) / 60);
        const timePrice: number = totalHours * 10;
        const materialPriceValue: number = Number(materialPrice.value) || 0;
        const patternPriceValue: number = Number(patternPrice.value) || 0;

        const totalPriceEUR: number = Math.ceil(timePrice + materialPriceValue + patternPriceValue);

        const currencyChoice: Currency = currency.value as Currency;
        const convertedTotalPrice: number = Math.ceil(totalPriceEUR * convertionRate[currencyChoice]);
        const currencySymbolChoice: string = currencySymbol[currencyChoice];

        priceResult.textContent = `Ta peluche ${plushieName.value} devrait coûter environ ${convertedTotalPrice}${currencySymbolChoice} ! ✨`
    });

    currency.addEventListener('change', () => {
        plushieForm.requestSubmit();
    });
})();
