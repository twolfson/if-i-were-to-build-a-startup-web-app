import { render, screen } from "@testing-library/react";
import { ReactApp } from "./ReactApp";

test.skip("renders content", () => {
  render(<ReactApp />);
  const content = screen.getByText(/Hello/i);
  expect(content).toBeInTheDocument();
});
