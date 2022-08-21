
const formId = "save-later-form";
const url = location.href;
const formIdentifier = `${url} ${formId}`;
const saveButton = document.querySelector("#save");
const alertBox = document.querySelector(".alert");
let form = document.querySelector(`#${formId}`);
let formElements = form.elements;


const getFormData = () => {
  let data = { [formIdentifier]: {} };
  for (const element of formElements) {
    if (element.name.length > 0) {
      data[formIdentifier][element.name] = element.value;
    }
  }
  return data;
};

saveButton.onclick = event => {
  event.preventDefault();
  data = getFormData();
  localStorage.setItem(formIdentifier, JSON.stringify(data[formIdentifier]));
  const message = "Form draft has been saved!";
  displayAlert(message);
};


const displayAlert = message => {
  alertBox.innerText = message;
  alertBox.style.display = "block";
  setTimeout(function() {
    alertBox.style.display = "none";
  }, 1000);
};


const populateForm = () => {
  if (localStorage.key(formIdentifier)) {
    const savedData = JSON.parse(localStorage.getItem(formIdentifier)); // get and parse the saved data from localStorage
    for (const element of formElements) {
      if (element.name in savedData) {
        element.value = savedData[element.name];
      }
    }
    const message = "Form has been refilled with saved data!";
    displayAlert(message);
  }
};

document.onload = populateForm(); // populate the form when the document is loaded