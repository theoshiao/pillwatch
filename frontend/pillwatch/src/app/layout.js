import "./globals.css";
import BasicExample from "./components/navbar";
import Login from "./components/Login";
import { Inter } from "next/font/google";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "Pillwatch",
  description: "From the creators of broceries",
};


export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head />
      <body className={inter.className}>
        <BasicExample />
        {children}
        <Login />
      </body>
    </html>
  );
}
