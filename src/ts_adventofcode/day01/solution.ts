import { readFile } from 'fs/promises'

async function main() {
    const path: string = "../../bld/inputs/aoc2024/day01/inputs.txt"
    const encoding: BufferEncoding = "utf-8"
    try {
        const data = await readFile(path, encoding)
        const matrix = parseData(data)
        const total = calculateTotalAbsDistance(matrix)
        console.log("Total abs distance:", total)
    } catch (err) {
        console.error("Error reading file:", err)
    }

}

function parseData(raw: string): number[][] {
    return raw
        .trim()
        .split("\n")
        .map(line => line.trim().split(/\s+/).map(Number))
}

function calculateTotalAbsDistance(matrix: number[][]): number {
    const numRows = matrix.length
    const numCols = matrix[0].length

    const sortedMatrix: number[][] = Array.from({ length: numRows }, () =>
        Array(numCols).fill(0)
    )

    for (let col = 0; col < numCols; col++) {
        const column = matrix.map(row => row[col]).sort((a, b) => a - b)

        for (let row = 0; row < numRows; row++) {
            sortedMatrix[row][col] = column[row]
        }
    }

    let total = 0
    for (const row of sortedMatrix) {
        for (let i = 0; i < row.length - 1; i++) {
            total += Math.abs(row[i] - row[i + 1])
        }
    }
    return total
}
main()