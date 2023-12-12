import React from 'react';

function ButtonComponent({ onClick, children }) {
  return (
    <button onClick={onClick}>
      {children}
    </button>
  );
}

export default ButtonComponent;