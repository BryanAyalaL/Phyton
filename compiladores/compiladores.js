let expresion = "a+b*c-(a+a)"; // Cambia esta cadena para probar diferentes casos
let caracteres = expresion.split("");
let pila = ["S"]; // Símbolo inicial de la gramática
let i = 0;
let rechazo = false;

console.log("Estado inicial de la pila:", pila);

while (i < caracteres.length && !rechazo) {
  let caracter = caracteres[i];
  let tope = pila[pila.length - 1];
  let avanzar = true;

  console.log(`\nProcesando carácter '${caracter}' con tope de pila '${tope}':`);

  switch (tope) {
    case "S": // Regla 1: S = AB
      console.log("Aplicando: S -> AB");
      pila.pop();
      pila.push("B", "A");
      avanzar = false;
      break;

    case "B": // Reglas 2, 3, 4: B = +AB | -AB | ε
      if (caracter === "+") {
        console.log("Aplicando: B -> +AB");
        pila.pop();
        pila.push("B", "A", "+");
      } else if (caracter === "-") {
        console.log("Aplicando: B -> -AB");
        pila.pop();
        pila.push("B", "A", "-");
      } else {
        console.log("Aplicando: B -> ε");
        pila.pop();
      }
      avanzar = false;
      break;

    case "A": // Regla 5: A = CD
      console.log("Aplicando: A -> CD");
      pila.pop();
      pila.push("D", "C");
      avanzar = false;
      break;

    case "D": // Reglas 6, 7, 8: D = *CD | /CD | ε
      if (caracter === "*") {
        console.log("Aplicando: D -> *CD");
        pila.pop();
        pila.push("D", "C", "*");
      } else if (caracter === "/") {
        console.log("Aplicando: D -> /CD");
        pila.pop();
        pila.push("D", "C", "/");
      } else {
        console.log("Aplicando: D -> ε");
        pila.pop();
      }
      avanzar = false;
      break;

    case "C": // Regla 9: C = F
      console.log("Aplicando: C -> F");
      pila.pop();
      pila.push("F");
      avanzar = false;
      break;

    case "F": // Reglas 10, 11: F = (S) | i
      if (caracter === "(") {
        console.log("Aplicando: F -> (S)");
        pila.pop();
        pila.push(")", "S", "(");
        avanzar = false;
      } else if (/[a-z]/i.test(caracter)) {
        console.log("Aplicando: F -> i");
        pila.pop();
        avanzar = true;
      } else {
        console.log(`Rechazo: '${caracter}' no es válido para F`);
        rechazo = true;
      }
      break;

    case "+": // Avanzar si coincide con '+'
    case "-":
    case "*":
    case "/":
    case "(":
    case ")":
      if (caracter === tope) {
        console.log(`Desapilando y avanzando para '${caracter}'`);
        pila.pop();
        avanzar = true;
      } else {
        console.log(`Rechazo: Se esperaba '${tope}', pero se encontró '${caracter}'`);
        rechazo = true;
      }
      break;

    default:
      console.log(`Rechazo: Símbolo '${tope}' no es válido`);
      rechazo = true;
      break;
  }

  if (avanzar) i++;
}

if (!rechazo) {
  while (pila.length > 0) {
    let tope = pila.pop();
    if (["A", "B", "C", "D", "F", "S"].includes(tope)) {
      console.log(`Procesando epsilon para '${tope}'`);
    } else {
      console.log(`Rechazo: Quedó '${tope}' en la pila`);
      rechazo = true;
      break;
    }
  }
}

if (!rechazo && pila.length === 0 && i === caracteres.length) {
  console.log("\nCadena aceptada. La pila está vacía.");
} else {
  console.log("\nCadena rechazada. La pila no se vació correctamente.");
}
