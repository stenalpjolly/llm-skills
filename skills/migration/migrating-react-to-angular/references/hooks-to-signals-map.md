# React Hooks to Angular 17+ Signals Mapping Reference

## State Management

| React Pattern | Angular 17+ Signal equivalent |
| :--- | :--- |
| `const [count, setCount] = useState(0)` | `count = signal(0);` |
| `setCount(5)` or `setCount(c => c + 1)` | `this.count.set(5);` or `this.count.update(c => c + 1);` |
| `count` (read) | `this.count()` (read signal as function execution) |

## Derived State / Performance Optimization

| React Pattern | Angular 17+ computed equivalent |
| :--- | :--- |
| `const double = useMemo(() => count * 2, [count])` | `double = computed(() => this.count() * 2);` |

## Side Effects

| React Pattern | Angular 17+ effect equivalent |
| :--- | :--- |
| `useEffect(() => { console.log(count) }, [count])` | `constructor() { effect(() => { console.log(this.count()); }); }` |

## Standard Event Handlers
- React: `onClick={handleClick}` -> Angular: `(click)="handleClick()"`
- React: `onChange={(e) => setValue(e.target.value)}` -> Angular (using reactive form or template-driven): `(input)="setValue($event)"`
