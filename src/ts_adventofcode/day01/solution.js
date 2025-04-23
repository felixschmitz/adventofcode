import { readFile } from 'fs/promises';
async function main() {
    const path = "../../bld/inputs/aoc2024/day01/sample.txt";
    const encoding = "utf-8";
    try {
        const data = await readFile(path, encoding);
        console.log(data);
    }
    catch (err) {
        console.error("Error reading file:", err);
    }
}
main();
