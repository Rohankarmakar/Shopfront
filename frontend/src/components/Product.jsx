import React from 'react';
import { Card } from 'react-bootstrap';
import Rating from './Rating';
import { Link } from 'react-router-dom';

const Product = ({ product }) => {
  return (
    <Card className="my-3 p-3 rounded">
      <Link to={`product/${product._id}`}>
        <Card.Img src={product.image} />
      </Link>

      <Card.Body>
        <Link to={`product/${product._id}`}>
          <Card.Title as="div">
            <strong>{product.name}</strong>
          </Card.Title>
        </Link>

        <Card.Text as="div">
          <div className="my-3">
            <Rating
              value={product.rating}
              text={`${product.numReviews} reviews`}
              color={'#f8e825'}
            />
          </div>
        </Card.Text>
        <Card.Text as="h3">&#8377;{product.price}</Card.Text>
      </Card.Body>

      <Card.Footer className="text-center">
        <button className="btn btn-primary my-3 mx-auto rounded">
          <i className="fa-solid fa-cart-plus"> Add to Cart </i>
        </button>
      </Card.Footer>
    </Card>
  );
};

export default Product;
