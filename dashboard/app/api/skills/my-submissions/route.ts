import { NextResponse } from "next/server"

// For local use there is no submission queue — skills are installed immediately.
export async function GET() {
  return NextResponse.json({ submissions: [] })
}
