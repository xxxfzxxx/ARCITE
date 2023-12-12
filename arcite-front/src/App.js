import React, { useState } from 'react';
import Header from './components/Header';
import InputComponent from './components/InputComponent';
import ButtonComponent from './components/ButtonComponent';
import DisplayComponent from './components/DisplayComponent';
import Footer from './components/Footer';
import axios from 'axios';

function App() {
  const [inputText, setInputText] = useState('');
  const [citationStyle, setCitationStyle] = useState('APA');
  const [citation, setCitation] = useState('');
  const [isLoading, setIsLoading] = useState(false); // Add a loading state

  const handleCitationStyleChange = (style) => {
    setCitationStyle(style);
  };

  const handleGenerateCitations = async () => {
    setIsLoading(true); // Start loading
    try {
      const response = await axios.post('http://127.0.0.1:5000/generate_citation', {
        text: inputText,
        style: citationStyle
      });
      setCitation(response.data.citation);
    } catch (error) {
      console.error('Error during citation generation:', error);
      alert('There was an error generating the citation.'); // Show error alert
    }
    setIsLoading(false); // Stop loading regardless of outcome
  };

  return (
    <div className="App">
      <Header />
      <InputComponent value={inputText} onChange={(value) => setInputText(value)} />{/* Ensure the onChange handler is set correctly */}
      <div>
        <ButtonComponent onClick={() => handleCitationStyleChange('APA')}>APA</ButtonComponent>
        <ButtonComponent onClick={() => handleCitationStyleChange('MLA')}>MLA</ButtonComponent>
        <ButtonComponent onClick={() => handleCitationStyleChange('IEEE')}>IEEE</ButtonComponent>
      </div>
      <ButtonComponent onClick={handleGenerateCitations}>Generate Citation</ButtonComponent>
      {isLoading ? <p>Loading...</p> : <DisplayComponent citation={citation} />} {/* Conditional rendering for loading indicator */}
      <Footer />
    </div>
  );
}

export default App;
