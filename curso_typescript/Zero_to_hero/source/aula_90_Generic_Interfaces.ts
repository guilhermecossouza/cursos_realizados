export {}

interface Person<T, U> {
    name: T;
    age: U;
}

const person : Person<string, string> = {
    name: "Guilherme",
    age: "40"
}

const person1: Person<boolean, boolean> = {
    name: true,
    age: true
}

//=> exemplo 02

interface FetchResponse<T> {
    data: T;
    status: number;
    statusText: string;
    headers: Record<string, string>;
}

async function fetchJson<T>(url: string): Promise<FetchResponse<T>> {
    const response = await fetch(url);
    const headers: Record<string, string> = {};
    response.headers.forEach((value, key) => {
        headers[key] = value
    });

    const data = await response.json();

    return {
        data: data as T,
        status: response.status,
        statusText: response.statusText,
        headers
    };
}

(async () => {
    const response = await fetchJson<{ userId: number, title: string, completed: boolean }>("https://jsonplaceholder.typicode.com/todos/1");
    console.log(response.data.userId);
    console.log(response.data.title);
    console.log(response.data.completed);
})();