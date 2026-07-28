(function () {
    const converterForm=document.getElementById("converterForm") as HTMLFormElement | null;
    const inputTemperature=document.getElementById("inputTemperature") as HTMLInputElement | null;
    const unit=document.getElementById("unit") as HTMLSelectElement | null;
    const converterResult=document.getElementById("converterResult") as HTMLDivElement | null;

    // Protection TypeScript contre les valeurs nulles
    if (!converterForm || !inputTemperature || !unit || !converterResult) {
        return;
    }

    // On peut aussi créer un type personnalisé (ou un Type Alias) pour nos unités !
    type UnitChoice = "F-to-C" | "C-to-F";

    converterForm.addEventListener('submit', (event: SubmitEvent) => {
        event.preventDefault();

        const temperature: number = Number(inputTemperature.value);
        const unitChoice: UnitChoice = unit.value as UnitChoice;

        if(unitChoice === "F-to-C") {
            const celsius: number = (temperature - 32) * 5/9;
            converterResult.textContent = `${temperature}°F = ${celsius.toFixed(2)}°C`;
        } else if(unitChoice === "C-to-F") {
            const fahrenheit: number = (temperature * 9/5) + 32;
            converterResult.textContent = `${temperature}°C = ${fahrenheit.toFixed(2)}°F`;
        }
    })
})();