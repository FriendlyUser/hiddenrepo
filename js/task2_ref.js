import React, { useState } from "react";
import ReactDOM from 'react-dom/client';
import { configureStore, createSlice } from '@reduxjs/toolkit';
import { Provider, useSelector, useDispatch } from "react-redux";
import { useAutoAnimate } from "@formkit/auto-animate/react";
import { nanoid } from "nanoid";

// Define the todos slice
const todoItems = localStorage.getItem("todos")
  ? JSON.parse(localStorage.getItem("todos"))
  : [];

export const todoSlice = createSlice({
  name: "todos",
  initialState: { todos: todoItems },
  reducers: {
    ekle: (state, action) => {
      if (action.payload !== "") {
        state.todos = [
          {
            id: nanoid(),
            gorev: action.payload,
            durum: false,
            tarih: new Date().toLocaleDateString(), // Add creation date
          },
          ...state.todos,
        ];
      }
      localStorage.setItem("todos", JSON.stringify(state.todos));
    },
    sil: (state, action) => {
      state.todos = state.todos.filter((t) => t.id !== action.payload);
      localStorage.setItem("todos", JSON.stringify(state.todos));
    },
    degistir: (state, action) => {
      state.todos = state.todos.map((item) =>
        item.id === action.payload ? { ...item, durum: !item.durum } : item
      );
      localStorage.setItem("todos", JSON.stringify(state.todos));
    },
  },
});

export const { ekle, sil, degistir } = todoSlice.actions;

// Store configuration
export const store = configureStore({
  reducer: {
    todos: todoSlice.reducer,
  },
});

function App() {
  const todos = useSelector((state) => state.todos.todos);
  const dispatch = useDispatch();
  const [todo, setTodo] = useState("");
  const [animation] = useAutoAnimate();
  const [isEmpty, setIsEmpty] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    dispatch(ekle(todo));
    setTodo("");
    if (todo === "") {
      setIsEmpty(true);
      setTimeout(() => setIsEmpty(false), 1500);
    }
  };

  // Sort todos by date (newest to oldest)
  const sortedTodos = [...todos].sort((a, b) => {
    const dateA = new Date(a.tarih);
    const dateB = new Date(b.tarih);
    return dateB - dateA;
  });

  return (
    <div className="max-w-xl mobil:px-4 mx-auto py-4">
      <h1 className="mb-8 text-center text-2xl font-bold">
        Yapılacaklar Listesi
      </h1>
      <form className="flex gap-x-4 mr-1" onSubmit={handleSubmit}>
        <input
          className="border rounded flex-1 indent-2 h-10"
          autoFocus
          type="text"
          placeholder="Bir görev yazın"
          onChange={(e) => setTodo(e.target.value)}
          value={todo}
        />
        <button
          className="bg-teal-600 text-white px-3 h-10 rounded"
          type="submit"
        >
          Ekle
        </button>
      </form>
      <ul
        className="h-[68vh] mt-4 overflow-y-auto md:scroll"
        ref={animation}
      >
        {isEmpty && (
          <li className="h-12 mr-1 text-red-700 flex items-center px-4 bg-red-100 rounded">
            Bir görev girin.
          </li>
        )}
        {todos.length === 0 && !isEmpty ? (
          <li className="h-12 mr-1 text-yellow-700 flex items-center px-4 bg-yellow-100 rounded">
            Hiç görev yok.
          </li>
        ) : null}
        {sortedTodos.map((item) => ( // Use sortedTodos here
          <li
            className="bg-green-300 rounded flex items-center justify-between h-[7.5vh] px-3 mt-[2.16vh] mr-1"
            key={item.id}
          >
            <span
              className={`text-green-700 ${
                item.durum ? "text-decoration-line: line-through" : ""
              }`}
              onClick={() => dispatch(degistir(item.id))}
            >
              {item.gorev} - {item.tarih} {/* Display the date */}
            </span>
            <span
              onClick={() => dispatch(sil(item.id))}
              className="px-4 py-1 rounded bg-red-600 text-white cursor-pointer"
            >
              Sil
            </span>
          </li>
        ))}
      </ul>
    </div>
  );
}

function main() {
  const root = ReactDOM.createRoot(document.getElementById('root'));
  root.render(
    <React.StrictMode>
      <Provider store={store}>
        <App />
      </Provider>
    </React.StrictMode>
  );
}

// Assuming index.js is using ES6 module, here we would call main()
main();
