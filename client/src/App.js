import './App.css';

import React, { useState, useEffect } from 'react'
import axios from 'axios'

const App = () => {
  const [productData, setProductData] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/api-test')
      .then(res => {
        setProductData(res.data)
      })
  }, [])

  // DEV: Don't commit!
  useEffect(() => {
    console.log(productData)
  }, [productData])

  let elements = productData.map(product =>
    <div className='product-info' key={product.id}>
      <p><span className='product-label'>Name</span><br />{product.name}</p>
      <p><span className='product-label'>Price</span><br />{product.price}</p>
    </div>
  );

  return (
    <>
      <h1>API Call Test</h1>
      <div id='products'>
        {elements}
      </div>
    </>
  );
}

export default App;
