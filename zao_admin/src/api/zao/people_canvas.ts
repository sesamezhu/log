import type { ZaoPeopleType } from './types'

const rect_width = 150
const rect_height = 50

const drawArrow = (
  ctx: CanvasRenderingContext2D,
  fromX: number,
  fromY: number,
  toX: number,
  toY: number
) => {
  ctx.beginPath()
  ctx.moveTo(fromX, fromY)
  ctx.lineTo(toX, toY)

  const headLength = 10
  const angle = Math.atan2(toY - fromY, toX - fromX)
  ctx.lineTo(
    toX - headLength * Math.cos(angle - Math.PI / 6),
    toY - headLength * Math.sin(angle - Math.PI / 6)
  )
  ctx.moveTo(toX, toY)
  ctx.lineTo(
    toX - headLength * Math.cos(angle + Math.PI / 6),
    toY - headLength * Math.sin(angle + Math.PI / 6)
  )

  ctx.stroke()
}

export const canvas_draw = (ctx: CanvasRenderingContext2D, tree: ZaoPeopleType) => {
  // 定义矩形框的位置和大小
  const rectX = 50
  const rectY = 50

  // 绘制外接矩形框
  ctx.strokeStyle = 'black'
  ctx.strokeRect(rectX, rectY, rect_width, rect_height)

  // 显示名称
  const name = `${tree.last || ''}${tree.first || ''}`
  ctx.font = '16px Arial'
  ctx.fillText(name, rectX + 10, rectY + 30)

  // 假设父矩形框的位置
  const parentRectX = 1000
  const parentRectY = 50

  // 绘制箭头
  drawArrow(
    ctx,
    rectX + rect_width,
    rectY + rect_height / 2,
    parentRectX,
    parentRectY + rect_height / 2
  )
  drawArrow(ctx, rectX, rectY + rect_height / 2, -50, parentRectY + rect_height / 2)
}
