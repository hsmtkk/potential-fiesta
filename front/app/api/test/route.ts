import { NextRequest, NextResponse } from "next/server";

export async function GET(req: NextRequest): Promise<NextResponse> {
    console.log("output env vars")
    console.log(process.env)
    return NextResponse.json({ env_vars: JSON.stringify(process.env) })
}