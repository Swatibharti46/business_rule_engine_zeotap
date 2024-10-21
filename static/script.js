const createRuleBtn = document.getElementById('create-rule-btn');
const combineRulesBtn = document.getElementById('combine-rules-btn');
const evaluateRuleBtn = document.getElementById('evaluate-rule-btn');
const resultElement = document.getElementById('result');

// Function to send API requests
async function sendApiRequest(url, data) {
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  });
  return await response.json();
}

// Create Rule
createRuleBtn.addEventListener('click', async () => {
  const ruleString = document.getElementById('rule-input').value;
  const response = await sendApiRequest('/api/rules', { rule: ruleString });
  resultElement.textContent = response.message;
});

// Combine Rules (Not implemented in this example - Logic needed in backend)
combineRulesBtn.addEventListener('click', () => {
  // Logic to get rules from UI and send to backend for combination
  resultElement.textContent = "Combine Rules feature not yet implemented."; 
});

// Evaluate Rule
evaluateRuleBtn.addEventListener('click', async () => {
  const userData = {
    age: parseInt(document.getElementById('age').value, 10),
    department: document.getElementById('department').value,
    salary: parseInt(document.getElementById('salary').value, 10),
    experience: parseInt(document.getElementById('experience').value, 10)
  };
  const response = await sendApiRequest('/api/rules/evaluate', { data: userData });
  resultElement.textContent = response.result ? "User is eligible" : "User is not eligible";
});