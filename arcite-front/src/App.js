import React, { useState } from 'react';
import Header from './components/Header';
import InputComponent from './components/InputComponent';
import ButtonComponent from './components/ButtonComponent';
import DisplayComponent from './components/DisplayComponent';
import Footer from './components/Footer';
import axios from 'axios';
import './App.css';

function App() {
  const [inputText, setInputText] = useState('');
  const [citationStyle, setCitationStyle] = useState('APA');
  const [citation, setCitation] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [processLog, setProcessLog] = useState(''); // State to store the complete process log

  const handleCitationStyleChange = (style) => {
    setCitationStyle(style);
  };

  const handleGenerateCitations = async () => {
    setIsLoading(true);
    setProcessLog(''); // Reset the process log
    try {
      const response = await axios.post('http://127.0.0.1:5000/generate_citation', {
        text: inputText,
        style: citationStyle
      });
      setCitation(response.data.citation);
      setProcessLog(response.data.steps.join("\n")); // Set the complete process log
    } catch (error) {
      console.error('Error during citation generation:', error);
      // Detailed error message
      const errorMessage = error.response ? 
        (error.response.data.error || error.response.data) : 
        error.message;
      alert(`There was an error generating the citation: ${errorMessage}`);
    }
    setIsLoading(false);
  };

  const handleCopyToClipboard = () => { 
    navigator.clipboard.writeText(citation).then(() => {
      alert('Citation copied to clipboard!');
    }).catch(err => {
      console.error('Could not copy text: ', err);
    });
  };

  const activeStyleButton = (styleName) => {
    // Updated to use CSS classes instead of inline styles
    return citationStyle === styleName ? 'button active' : 'button';
  };

  return (
    <div className="App">
      <Header />
      <InputComponent value={inputText} onChange={(e) => setInputText(e.target.value)} />
      <div>
        {/* Updated to use CSS classes for buttons */}
        <ButtonComponent className={activeStyleButton('APA')} onClick={() => handleCitationStyleChange('APA')}>APA</ButtonComponent>
        <ButtonComponent className={activeStyleButton('MLA')} onClick={() => handleCitationStyleChange('MLA')}>MLA</ButtonComponent>
        <ButtonComponent className={activeStyleButton('IEEE')} onClick={() => handleCitationStyleChange('IEEE')}>IEEE</ButtonComponent>
      </div>
      <ButtonComponent className="button" onClick={handleGenerateCitations}>Generate Citation</ButtonComponent>
      {isLoading ? <p>{processLog || 'Loading...'}</p> : <DisplayComponent citation={citation} />}
      {processLog && <div><p>Process Log:</p><p>{processLog}</p></div>}
      {citation && <ButtonComponent className="button" onClick={handleCopyToClipboard}>Copy to Clipboard</ButtonComponent>}
      <Footer />
    </div>
  );
}

export default App;
