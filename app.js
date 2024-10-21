import React, { useState } from 'react';
import './App.css'; 

function App() {
  const [rules, setRules] = useState([
    "((age > 30 AND department == 'Sales') OR (age < 25 AND department == 'Marketing')) AND (salary > 50000 OR experience > 5)",
    "((age > 30 AND department == 'Marketing')) AND (salary > 20000 OR experience > 5)",
  ]);
  const [newRule, setNewRule] = useState('');
  const [userData, setUserData] = useState({
    age: '',
    department: '',
    salary: '',
    experience: '',
  });
  const [evaluationResult, setEvaluationResult] = useState('');

  const handleAddRule = () => {
    if (newRule.trim() !== '') {
      setRules([...rules, newRule]);
      setNewRule('');
    }
  };

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setUserData({ ...userData, [name]: value });
  };

  const handleEvaluate = async () => {
    try {
      const response = await fetch('http://localhost:5000/evaluate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ rules: rules, data: userData }),
      });

      const data = await response.json();
      setEvaluationResult(data.result ? 'Match!' : 'No Match'); 
    } catch (error) {
      console.error('Evaluation error:', error);
      setEvaluationResult('An error occurred'); 
    }
  };

  return (
    <div className="container">
      <div className="header">
        <h1>Business Rules Engine</h1>
      </div>

      <div className="rules-section">
        <h2>Rules</h2>
        <ul>
          {rules.map((rule, index) => (
            <li key={index}>{rule}</li>
          ))}
        </ul>
        <div className="add-rule">
          <input
            type="text"
            value={newRule}
            onChange={(e) => setNewRule(e.target.value)}
            placeholder="Enter a new rule..."
          />
          <button onClick={handleAddRule}>Add Rule</button>
        </div>
      </div>

      <div className="user-data-section">
        <h2>User Data</h2>
        <div className="input-group">
          <label htmlFor="age">Age:</label>
          <input
            type="number"
            id="age"
            name="age"
            value={userData.age}
            onChange={handleInputChange}
          />
        </div>
        <div className="input-group">
          <label htmlFor="department">Department:</label>
          <input
            type="text"
            id="department"
            name="department"
            value={userData.department}
            onChange={handleInputChange}
          />
        </div>
        <div className="input-group">
          <label htmlFor="salary">Salary:</label>
          <input
            type="number"
            id="salary"
            name="salary"
            value={userData.salary}
            onChange={handleInputChange}
          />
        </div>
        <div className="input-group">
          <label htmlFor="experience">Experience:</label>
          <input
            type="number"
            id="experience"
            name="experience"
            value={userData.experience}
            onChange={handleInputChange}
          />
        </div>
        <button onClick={handleEvaluate}>Evaluate</button>
      </div>

      <div className="results-section">
        <h2>Evaluation Result:</h2>
        <p className={`result ${evaluationResult === 'Match!' ? 'match' : 'no-match'}`}>
          {evaluationResult} 
        </p>
      </div>
    </div>
  );
}

export default App;
