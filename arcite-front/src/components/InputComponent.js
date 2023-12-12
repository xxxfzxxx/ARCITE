import React from 'react';

function InputComponent({ value, onChange }) {
  return (
    <textarea
      placeholder="Paste the paragraph here"
      value={value}
      onChange={e => onChange(e.target.value)}
      style={{ width: '100%', height: '150px' }}
    />
  );
}

export default InputComponent;