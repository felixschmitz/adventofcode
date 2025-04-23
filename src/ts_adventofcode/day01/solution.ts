import { readFile } from 'fs/promises'

async function main() {
    const path: string = "../../bld/inputs/aoc2024/day01/inputs.txt"
    const encoding: BufferEncoding = "utf-8"
    try {
        const data = await readFile(path, encoding)
        const matrix = parseData(data)
        const solution1 = part1(matrix)
        console.log("Solution of part 1:", solution1)
        const solution2 = part2(matrix)
        console.log("Solution of part 2:", solution2)
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

function part1(matrix: number[][]): number {
    const total = calculateTotalAbsDistance(matrix)
    return total
}

function part2(matrix: number[][]): number {
    const left = matrix.map(row => row[0])
    const right = matrix.map(row => row[1])

    const leftFreq = countFrequencies(left)
    const rightFreq = countFrequencies(right)

    let total = 0
    for (const [value, countInLeft] of leftFreq.entries()) {
        const countInRight = rightFreq.get(value) ?? 0
        total += value * countInLeft * countInRight
    }
    return total
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


function countFrequencies(arr: number[]): Map<number, number> {
    const freq = new Map<number, number>()
    for (const x of arr) {
        freq.set(x, (freq.get(x) ?? 0) + 1)
    }
    return freq
}


main()