const display = document.getElementById("display");
const buttons = document.querySelectorAll("button");

let currentInput = "";

function isOperator(value) {
  return value === "+" || value === "-" || value === "×" || value === "÷";
}

function updateDisplay() {
  display.value = currentInput;
}

function clearCalculator() {
  currentInput = "";
  display.value = "";
}

function deleteLastCharacter() {
  currentInput = currentInput.slice(0, -1);
  updateDisplay();
}

function calculateResult() {
  try {
    if (currentInput === "") {
      return;
    }

    const lastChar = currentInput[currentInput.length - 1];

    if (isOperator(lastChar)) {
      currentInput = currentInput.slice(0, -1);
    }

    let expression = currentInput
      .replaceAll("×", "*")
      .replaceAll("÷", "/");

    let result = eval(expression);

    display.value = result;
    currentInput = result.toString();
  } catch {
    display.value = "Error";
    currentInput = "";
  }
}

function handleInput(value) {
  if (value === "C") {
    clearCalculator();
    return;
  }

  if (value === "⌫") {
    deleteLastCharacter();
    return;
  }

  if (value === "=") {
    calculateResult();
    return;
  }

  if (value === ".") {
    const numbers = currentInput.split(/[+\-×÷]/);
    const lastNumber = numbers[numbers.length - 1];

    if (lastNumber.includes(".")) {
      return;
    }

    if (currentInput === "" || isOperator(currentInput[currentInput.length - 1])) {
      currentInput += "0.";
    } else {
      currentInput += ".";
    }

    updateDisplay();
    return;
  }

  if (isOperator(value)) {
    if (currentInput === "") {
      return;
    }

    const lastChar = currentInput[currentInput.length - 1];

    if (isOperator(lastChar)) {
      currentInput = currentInput.slice(0, -1) + value;
    } else {
      currentInput += value;
    }

    updateDisplay();
    return;
  }

  currentInput += value;
  updateDisplay();
}

buttons.forEach(function(button) {
  button.addEventListener("click", function() {
    handleInput(button.textContent);
  });
});

document.addEventListener("keydown", function(event) {
  const key = event.key;

  if (key >= "0" && key <= "9") {
    handleInput(key);
  }

  if (key === ".") {
    handleInput(".");
  }

  if (key === "+") {
    handleInput("+");
  }

  if (key === "-") {
    handleInput("-");
  }

  if (key === "*") {
    handleInput("×");
  }

  if (key === "/") {
    event.preventDefault();
    handleInput("÷");
  }

  if (key === "Backspace") {
    handleInput("⌫");
  }

  if (key === "Enter" || key === "=") {
    event.preventDefault();
    handleInput("=");
  }

  if (key === "Escape") {
    handleInput("C");
  }
});