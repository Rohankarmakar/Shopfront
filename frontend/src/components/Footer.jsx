import React from 'react';
import { Container, Row, Col } from 'react-bootstrap';

const Footer = () => {
  return (
    <footer className="bg-dark text-white py-3 mt-auto">
      <Container>
        <Row>
          <Col className="text-center">
            <p>
              &copy; {new Date().getFullYear()} Shopfront. All rights reserved.
            </p>
          </Col>
        </Row>
      </Container>
    </footer>
  );
};

export default Footer;
